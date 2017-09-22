import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Number of neighbours       0  1  2  3  4  5  6  7  8
RULE_OF_SURVIVAL = np.array([0, 0, 1, 1, 0, 0, 0, 0, 0])
RULE_OF_CREATION = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0])

# Map resolution
MAP_SIZE = 100

# Map creation
gof_map = np.random.choice([0, 1], size=(MAP_SIZE, MAP_SIZE))

# Initialize plotting
fig, ax = plt.subplots()
img = ax.imshow(gof_map)
plt.show(block=False)

# Helper function for map drawing
def draw_map(gof_map):
    img.set_data(gof_map)
    fig.canvas.draw()
    fig.canvas.flush_events()

# This filter helps to count rank of life
gof_filter = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

while True:
    # Generate rank for each cell using image filtering
    rank_map = signal.convolve2d(gof_map, gof_filter, boundary='wrap', mode='same')

    # Find out which cells matches with the rules
    gof_map = RULE_OF_CREATION[rank_map] | gof_map & RULE_OF_SURVIVAL[rank_map]

    # Refresh the map   
    draw_map(gof_map)
