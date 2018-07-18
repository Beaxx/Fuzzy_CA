import config
import Inference as Inf
from Cell import Cell
from typing import List
import GraphicsUnit as Gu

class Grid:
    def __init__(self):
        self.width = config.grid_width
        self.height = config.grid_height
        self.cell_size = int(config.window_width / self.width)
        self.cells = []  # type: List[List[Cell]]
        self.initialize()

    # Outer Cells are Crisp, Inner Cells are Fuzzy
    def initialize(self):
        for row in range(0, self.height):
            self.cells.append([])
            for col in range(0, self.width):
                if row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1:
                    self.cells[row].append(Cell(0))
                else:
                    self.cells[row].append(Cell(1))

    def create_fuzzy(self):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if not (row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1):
                    self.cells[row][col].fuzzy_value = Inf.affiliation_function(self, row, col)

    def defuzz(self, window):
        for row in range(0, self.height):
            for col in range(0, self.width):
                if not (row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1):
                    no = self.cells[row][col].fuzzy_value[0]
                    abst = self.cells[row][col].fuzzy_value[1]
                    yes = self.cells[row][col].fuzzy_value[2]

                    if no > yes and no > abst:
                        defuzz = -1
                    elif yes > no and yes > abst:
                        defuzz = 1
                    else:
                        defuzz = 0

                    self.cells[row][col].fuzzy = 0
                    self.cells[row][col].value = defuzz

                    Gu.draw_crisp_cell(window, self, row, col, self.cells[row][col])

    @staticmethod
    def select_cells(grid, row, col):

        # Normal
        if (0 < row < grid.height-1) and (0 < col < grid.width-1):
            return[[row - 1, col], [row - 1, col - 1], [row, col - 1], [row + 1, col - 1], [row + 1, col],
                   [row + 1, col + 1], [row, col + 1], [row - 1, col + 1]]

        # Top Left Corner
        elif 0 == row and col == 0:
            return [[grid.height-1, col], [grid.height-1, grid.width-1], [row, grid.width-1],
                    [row + 1, grid.width-1], [row + 1, col], [row + 1, col + 1], [row, col + 1],
                    [grid.height-1, col + 1]]

        # Top Border
        elif 0 == row and (0 < col < grid.width-1):
            return [[grid.height-1, col], [grid.height-1, col-1], [row, col - 1], [row + 1, col - 1],
                    [row + 1, col], [row + 1, col + 1], [row, col + 1], [grid.height-1, col + 1]]

        # Top Right Corner
        elif 0 == row and col == grid.width-1:
            return [[grid.height-1, col], [grid.height-1, col - 1], [row, col - 1], [row + 1, col - 1],
                    [row + 1, col], [row + 1, 0], [row, 0], [grid.height-1, 0]]

        # Left Border
        elif (0 < row < grid.height-1) and 0 == col:
            return [[row - 1, col], [row - 1, grid.width-1], [row, grid.width-1],
                    [row + 1, grid.width-1], [row + 1, col], [row + 1, col + 1], [row, col + 1],
                    [row - 1, col + 1]]

        # Right Border
        elif (0 < row < grid.height-1) and col == grid.width-1:
            return [[row - 1, col], [row - 1, col - 1], [row, col - 1], [row + 1, col - 1], [row + 1, col],
                    [row + 1, 0], [row, 0], [row - 1, 0]]

        # Bottom Left Corner
        elif grid.height-1 == row and 0 == col:
            return [[row - 1, col], [row - 1, grid.width-1], [row, grid.width-1], [0, grid.width-1],
                    [0, col], [0, col + 1], [row, col + 1], [row - 1, col + 1]]

        # Bottom Border
        elif (grid.height-1 == row) and (0 < col < grid.width-1):
            return [[row - 1, col], [row - 1, col - 1], [row, col - 1], [0, col - 1], [0, col], [0, col + 1],
                    [row, col + 1], [row - 1, col + 1]]

        # Bottom Right Corner
        elif (grid.height-1 == row) and (grid.width-1 == col):
            return [[row - 1, col], [row - 1, col - 1], [row, col - 1], [0, col - 1], [0, col], [0, 0],
                    [row, 0], [row - 1, 0]]

#     def add_up_environment(self, row, col):
#         value = 0
#
#         environment = self.select_cells()
#
#         for i, element in enumerate(environment):
#             value += De.defuz(self.cells[environment[i][0]][environment[i][1]])
# >