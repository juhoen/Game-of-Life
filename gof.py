import matplotlib.pyplot as plt
from scipy import signal
import numpy as np

# Number of neighbours:      0  1  2  3  4  5  6  7  8
RULE_OF_SURVIVAL = np.array([0, 0, 1, 1, 0, 0, 0, 0, 0])
RULE_OF_CREATION = np.array([0, 0, 0, 1, 0, 0, 0, 0, 0])

# Number of cells on x and y axis
MAP_SIZE = 200

# Helper function for map drawing
def draw_map(map):
    plt.clf()
    plt.imshow(map)
    plt.pause(0.05)

# This filter helps to count rank of life
rank_filter = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
])

# Generate random map
map = np.random.choice([0, 1], size=(MAP_SIZE, MAP_SIZE))

# Simulation loop
while True:
    # Generate rank for each cell using image filtering
    rank_map = signal.convolve2d(map, rank_filter, boundary='wrap', mode='same')

    # Find out which cells matches with the rules
    map = RULE_OF_SURVIVAL[rank_map] & RULE_OF_CREATION[rank_map] | map & RULE_OF_SURVIVAL[rank_map]
    
    # Refresh the map   
    draw_map(map)
