from Grid import Grid


def affiliation_function(grid, row, col):
    surrounding_coords = Grid.select_cells(grid, row, col)

    environment_value = 0
    environment_count = 0
    for coord in surrounding_coords:
        if grid.cells[coord[0]][coord[1]].value is not None:
            environment_count += 1
            environment_value += grid.cells[coord[0]][coord[1]].value
    environment_avg = environment_value / environment_count
    return [no_function(environment_avg), abst_function(environment_avg), yes_function(environment_avg)]


def no_function(moore_value):
    if -1 <= moore_value <= 0:
        return -moore_value
    else:
        return 0  # Moore_value < -1 does not need to be catched


# # Abstiantion function with slope 1 / -1
# def abst_function(moore_value):
#     if -1 <= moore_value <= 0:
#         return moore_value * (-1)
#     elif 0 < moore_value <= 1:
#         return (moore_value - 1) * (-1)
#     else:
#         return 0

# Abstiantion function with slope 2 / -2
def abst_function(moore_value):
    if -0.5 <= moore_value < 0.0:
        return 2 * moore_value + 1
    elif 0.0 < moore_value <= 0.5:
        return -2 * moore_value + 1
    elif moore_value == 0.0:
        return 1
    else:
        return 0


def yes_function(moore_value):
    if 0 <= moore_value <= 1:
        return moore_value
    else:
        return 0  # Moore_value > 1 does not need to be catched

