import config
import random as rnd


class Cell:
    def __init__(self, is_fuzzy):
        """
        Zelle ist entweder Fuzzy oder Crisp.
        Fuzzy: Zelle hat keinen festen Wert und hält eine Liste an Fuzzy Werten entsprechend ihrer Zugehörigkeit
        Crisp: Zelle wird entsprechend config ein zufälliger Wert zugeordnet
        :param is_fuzzy: 1:Ja oder 0:Nein
        """
        if is_fuzzy is 1:  # Fuzzy
            self.fuzzy = 1
            self.value = None
            self.fuzzy_value = []
        else:  # Crisp
            self.fuzzy = 0
            rnd_val = rnd.uniform(0.0, 1.0)
            if config.cell_prop[0] > rnd_val:
                self.value = 1.0
            if config.cell_prop[1] > rnd_val:
                self.value = 0.0
            if config.cell_prop[2] >= rnd_val:
                self.value = -1.0
