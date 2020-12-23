from scipy.spatial import distance

# Model a flock of birds according to Reynolds rules

# 2D model:

#Data:
# A list of tuples with x,y positions
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
# check if new positions are possible, if not. Try a different position by slightly adjusting heading


# Display:
# Scatterplot?
# Matplotlib

