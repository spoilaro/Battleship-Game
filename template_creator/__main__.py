import numpy as np


# Write your own ship placements here for the templates
# raw_list_grid = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [1, 1, 0, 0, 0, 0, 4, 4, 4, 4],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 2, 2, 2, 0, 0, 0, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],
# ]
raw_list_grid = [
    [0, 0, 0, 0, 4, 4, 4, 4, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 2, 2, 2, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 0, 0, 0],
]

# Conver to 2D numpy array
grid_array = np.array(raw_list_grid, dtype=int)

# Serialize the grid
byte_grid = grid_array.tobytes()

template_name = input("Template name: ")

with open(f"templates/{template_name}", "wb") as f:
    f.write(byte_grid)

print(
    "Template serialized and saved to\033[1m /templates\033[0m directory")
