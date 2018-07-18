import config, ctypes
import GraphicsUnit as Gu
from Grid import Grid
from graphics import *


def main():
    window = GraphWin("Fuzzy CA", config.window_width, config.window_height)

    ctypes.windll.user32.MessageBoxW(0, "Simulation startet mit einem definierten Zustand der Moore Umgebung, "
                                        "Aus der Moore Umgebung wird die Zugehörigkeit der Zentral-Zelle zu den "
                                        "Sets '1','0' und '-1' bestimmt.\n"
                                        "Beim Klick in das Fenster wird die Zentral-Zelle defuzzifiziert.\n"
                                        "Ein erneuter Klick läd eine neue Moore-Umgebung und eine neue Simulation "
                                        "startet", "Program Ablauf", 0)

    while True:
        grid = Grid()
        grid.create_fuzzy()
        drawn_elements = Gu.draw_grid(window, grid)
        window.getMouse()
        grid.defuzz(window)
        window.getMouse()
        Gu.undraw_elements(drawn_elements)
main()


