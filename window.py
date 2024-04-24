from tkinter import *
from functools import partial


class window:
    """
    Класс для создания окна.\n
    Позволяет дочерним классам создавать новые окна и уничтожать их.\n
    """

    def __init__(self, root, title, width, height):
        self.root = root
        self.title = title
        self.width = width
        self.height = height
        self.window = None

    def create_new_window(self):
        self.window = Toplevel(self.root)
        self.window.title(self.title)
        self.window.geometry(
            f"{self.width}x{self.height}+{self.root.winfo_x()}+{self.root.winfo_y()}")
        self.window.protocol("WM_DELETE_WINDOW", partial(
            self.destroy_window))
        self.root.withdraw()

    def destroy_window(self):
        self.window.destroy()
        self.root.deiconify()
