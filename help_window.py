from tkinter import *
from tkinter import ttk
from window import window


class help_window(window):
    """
    Класс для создания окна помощи.
    Наследует класс `window`, чтобы использовать его методы.
    """

    def set_help_window(self):
        """
        Метод для создания окна помощи.
        """
        self.create_new_window()
        label = ttk.Label(self.window, text="Help window")
        label.pack()
