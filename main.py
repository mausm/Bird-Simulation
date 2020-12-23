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
        self.positions = np.array([[0,0]])
        self.heading = np.array([[0,0]])

    def add_bird(self, board):
        # CHANGE THE LOW= HIGH= TO MAX SIZE OF BOARD
        xy = np.random.randint(low=1, high=1, size=(1,2))
        x,y = xy[0], xy[1]
        np.append(self.positions,[x,y], axis=0)
        np.append(self.heading,[0,0], axis=0)


def update_positions(boardsize, pos_arr, heading_list):
    # get avg position of the x/y positions of all birds
    avg_pos = np.mean(pos_arr, axis=1)
    avg_arr = np.repeat(avg_pos, len(pos_arr), axis=0)
    # get heading for each bird
    diff_arr = np.subtract(avg_pos,avg_arr)
    sum_arr = np.add(np.absolute(pos_arr[:,0]),np.absolute(pos_arr[:,1]))
    heading = np.divide(diff_arr, sum_arr)

    # add the heading to the old xy coordinates the current step is 1.
    # So it don't multiply the heading with a multiplier, but that is an easy change

    CUTOFF_DIST = 4
    KDTree.query(pos_arr,3, distance_upper_bound=CUTOFF_DIST)
