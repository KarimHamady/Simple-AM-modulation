import matplotlib.pyplot as plt
import math
import numpy as np

# define variables
min_x = -2
min_y = 2
number_of_points = 100000
points = []
k = 1/20

time = np.linspace(min_x, min_y, number_of_points)

# add points to the points array / draw the graph
for t in time:
    points.append(50*(1+k*20*math.cos(2*math.pi*t))*math.cos(100*math.pi*t))

# plot the graph
plt.scatter(time, points, color='blue')
plt.show()
