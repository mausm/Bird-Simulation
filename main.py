import matplotlib as plt
import numpy as np

from scipy.spatial import distance
from scipy.spatial import KDTree

# Model a flock of birds according to Reynolds rules

# 2D model:

#Data:
# A numpy array with x,y positions
# Same length list of tuples with directions (xdiff, ydiff)
# So each bird is the same index pos in both lists
# set up a class that has a position list and a direction list
# -1 can be left or down. 1 is right or up depending on x or y

# Calculations:
# calculate average position of all x,y pos
# calculate the average direction of local birds
# calculate the distance to closest neighbors (or all and select closest)

# Steps in calc
# step 1 get the direction to get to the avg position
# step 2 get the direction of the closest neighbors
# use the average direction as heading
# check if new positions are possible, if not. Try a different position by slightly adjusting heading/speed


# Display:
# Scatterplot?
# Matplotlib

class BirdFlock:
    def __init__(self):
        self.positions = np.empty((0,2), int)
        self.heading = np.empty((0,2), float)
        self.obstacles = np.empty((0,2), int)

    def add_bird(self, board_max):
        # square board so x and y are the same max
        xy = np.random.randint(low=0, high=board_max, size=2)
        # numpy isin works weird, so we convert back to native python lists
        checklist = self.positions.tolist()
        if xy.tolist() not in checklist:
            self.positions = np.append(self.positions,[xy], axis=0)

            start_heading = 2 * np.random.random_sample(2,) - 1
            self.heading = np.append(self.heading,[start_heading], axis=0)


def update_headings(boardmax, pos_arr, heading_list):
    # Tree for the closest neighbors
    tree = KDTree(pos_arr, leafsize=100000)

    movement = np.array([])

    cutoff_dist = 10
    cutoff_amount_birds = 5
    local_birds = 3
    local_dist = 4
    min_dist = 0.5
    for i in range(len(pos_arr)):
        bird = pos_arr[i]
        # results is an array of distances and positions
        results = tree.query(bird, cutoff_amount_birds, distance_upper_bound=cutoff_dist)

        distances = results[0][1:]
        locations = results[1][1:]

        # Rule 1, avoid others
        if min(results[0] < min_dist):
            direct_neighbor_index = np.where(distances == min(distances))[0][0]
            dist = np.subtract(bird, pos_arr[direct_neighbor_index])

            #WALK THROUGH THIS PART
            heading = np.divide(dist, np.absolute(dist))
            heading_list[i] = heading

        # Rule 2 move in the same direction as neighbors
        local_headings = np.empty((0,2))

        # select only the 3 closest birds and cut off any
        for j in range(local_birds):
            if distances[j] < local_dist:
                local_headings = np.append(local_headings,[heading_list[locations[j]]], axis=0)

        # 50% percent is the old heading, 50 % is the nearby headings
        if len(local_headings) > 0:
            heading_list[i] = 0.5 * np.mean(local_headings, axis=0) + 0.5 * heading_list[i]

        # Rule 3 move towards the average position of the group
        avg_pos = np.mean(pos_arr[locations], axis=0)
        xydiff = np.subtract(avg_pos, bird)
        if np.sum(np.absolute(xydiff)) != 0:
            heading = np.divide(xydiff, np.sum(np.absolute(xydiff)))
        else:
            heading = heading_list[i]

        if len(heading) > 0:
            heading_list[i] = 0.2 * heading + 0.8 * heading_list[i]

        # Avoiding obstacles / wall should override previous values
        # So if the x goes negative the heading goes positive by taking absolute value
        if pos_arr[i][0] <= 0:
            heading_list[i][0] = abs(heading_list[i][0])
        elif pos_arr[i][0] >= boardmax:
            heading_list[i][0] = heading_list[i][0] * (-1)
        if pos_arr[i][1] <= 0:
            heading_list[i][1] = abs(heading_list[i][1])
        elif pos_arr[i][0] >= boardmax:
            heading_list[i][1] = heading_list[i][1] * (-1)

    return heading_list


def update_positions(pos_arry, heading_update):
    return np.add(pos_arry, heading_update)


def main():
    sim_data = BirdFlock()
    for i in range(20):
        sim_data.add_bird(10)

    while True:
        movement = update_headings(10,sim_data.positions,sim_data.heading)
        sim_data.positions = update_positions(sim_data.positions, movement)
        print(sim_data.positions)
        if input("continue? c: ") != "c":
            break


if __name__ == '__main__':
    main()
