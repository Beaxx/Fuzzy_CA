import config
import random as rnd


class Cell:
    def __init__(self, is_fuzzy):
        if is_fuzzy is 1:
            self.fuzzy = 1
            self.value = None
            self.fuzzy_value = []
        else:
            self.fuzzy = 0
            rnd_val = rnd.uniform(0.0, 1.0)
            if config.cell_prop[0] > rnd_val:
                self.value = 1.0
            if config.cell_prop[1] > rnd_val:
                self.value = 0.0
            if config.cell_prop[2] >= rnd_val:
                self.value = -1.0
