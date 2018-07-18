from graphics import *


def draw_grid_initial(window, grid):
    """
    Zeichnet das Raster in das geöffnete Fenster.
    :return Eindimensionales Jagged-Array mit allen gezeichneten Elementen
    """
    draw_on_screen = []
    for row in range(0, len(grid.cells)):
        for col in range(0, len(grid.cells[0])):
            if grid.cells[row][col].fuzzy == 0:
                draw_on_screen.append(draw_crisp_cell(window, grid, row, col, grid.cells[row][col]))
            else:
                draw_on_screen.append(draw_crisp_cell(window, grid, row, col, grid.cells[row][col]))
    return draw_on_screen


def draw_grid(window, grid):
    """
    Zeichnet das Raster in das geöffnete Fenster.
    :param window: Darstellungsfenster
    :param grid: Datenraster
    :return: Eindimensionales Jagged-Array mit allen gezeichneten Elementen
    """
    draw_on_screen = []
    for row in range(0, len(grid.cells)):
        for col in range(0, len(grid.cells[0])):
            if grid.cells[row][col].fuzzy == 0:
                draw_on_screen.append(draw_crisp_cell(window, grid, row, col, grid.cells[row][col]))
            else:
                draw_on_screen.append(draw_fuzzy_cell(window, grid, row, col, grid.cells[row][col]))
    return draw_on_screen


def draw_crisp_cell(window, grid, row, col, cell):
    """
    Erstellt die grafische Repräsentation einer Defuzzifizierten bzw. distinkten oder crispen Zelle

    :param window: Darstellungsfenster
    :param grid: Datenraster
    :param row: Reihe der Zelle
    :param col:  Zeile der Zelle
    :param cell: Zellen-Objekt
    :return: [Rechteck Grafikobjekt, Text Grafikobjekt]
    """
    p1 = Point(col * grid.cell_size, row * grid.cell_size)
    p2 = Point(col * grid.cell_size + grid.cell_size, row * grid.cell_size + grid.cell_size)

    # Cell Color
    color = None
    if cell.value is None:
        color = [245, 245, 245]
    elif cell.value == -1:
        color = [255, 69, 0]
    elif cell.value == 0:
        color = [255, 215, 0]
    elif cell.value == 1:
        color = [50, 205, 50]

    square = Rectangle(p1, p2)
    square.setFill(color_rgb(color[0], color[1], color[2]))
    square.setOutline("black")
    square.setWidth(1)

    txt = Text(Point(int(p1.getX()+grid.cell_size/2), int(p1.getY())+grid.cell_size/2), str(cell.value))
    txt.setSize(int(round(grid.cell_size / 4)))
    txt.setTextColor("black")

    square.draw(window)
    txt.draw(window)

    return square, txt


def draw_fuzzy_cell(window, grid, row, col, cell):
    """
        Erstellt die grafische Repräsentation einer Fuzzifizierten Zelle
    :param window: Darstellungsfenster
    :param grid: Datenraster
    :param row: Reihe der Zelle
    :param col:  Zeile der Zelle
    :param cell: Zellen-Objekt
    :return: [Oberes Rechteck Grafikobjekt,
                Mittleres Rechteck Grafikobjekt,
                Unteres Rechteck Grafikobjekt,
                Text Grafikobjekt]
    """

    # top rectangle - no
    p1t = Point(col * grid.cell_size, row * grid.cell_size)
    p2t = Point(col * grid.cell_size + grid.cell_size, row * grid.cell_size * 1/3 + grid.cell_size)

    square_top = Rectangle(p1t, p2t)
    square_top.setFill(color_rgb(255, 69, 0))
    square_top.setOutline("black")
    square_top.setWidth(2)

    # mid rectangle - indifferent
    p1m = Point(col * grid.cell_size, row * grid.cell_size + 1/3 * grid.cell_size)
    p2m = Point(col * grid.cell_size + grid.cell_size, row * grid.cell_size * 2 / 3 + grid.cell_size)

    square_mid = Rectangle(p1m, p2m)
    square_mid.setFill(color_rgb(255, 215, 0))
    square_mid.setOutline("black")
    square_mid.setWidth(2)

    # bottom rectangle - yes
    p1b = Point(col * grid.cell_size, row * grid.cell_size + 2 / 3 * grid.cell_size)
    p2b = Point(col * grid.cell_size + grid.cell_size, row * grid.cell_size + grid.cell_size)

    square_bot = Rectangle(p1b, p2b)
    square_bot.setFill(color_rgb(50, 205, 50))
    square_bot.setOutline("black")
    square_bot.setWidth(2)

    txt = Text(Point(int(p1t.getX() + grid.cell_size / 2), int(p1t.getY()) + grid.cell_size / 2),
               str(cell.fuzzy_value[0]) + "\n\n" +
               str(cell.fuzzy_value[1]) + "\n\n" +
               str(cell.fuzzy_value[2]))
    txt.setSize(int(round(grid.cell_size / 8)))
    txt.setTextColor("black")

    square_top.draw(window)
    square_mid.draw(window)
    square_bot.draw(window)
    txt.draw(window)

    return square_top, square_mid, square_bot, txt


def undraw_elements(drawn_elements):
    """
    Löscht Grafikelemente aus der Darstellungsansicht
    :param drawn_elements:
    :return:
    """
    for cell in drawn_elements:
        for element in cell:
            element.undraw()
