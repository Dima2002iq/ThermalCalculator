from tkinter import *


def create_grid_layout(root, num_columns, num_rows):
    """
    Функция для создания сетки в окне.

    Аргументы:
        root: Окно, в котором будет создана сетка.
        num_columns: Количество столбцов в сетке.
        num_rows: Количество строк в сетке.
    """

    for column in range(num_columns):
        root.columnconfigure(column, weight=1)
    for row in range(num_rows):
        root.rowconfigure(row, weight=1)
