from tkinter import *
from tkinter import ttk
from calculation_window import calculation_window
from help_window import help_window
from grid_layout import create_grid_layout

# region InitializeRoot
width = 350
height = 200
root = Tk()
root.title("Расчёт теплопотерь дома")
root.geometry(
    f"{width}x{height}+{root.winfo_screenwidth()//2 - width//2}+{root.winfo_screenheight()//2 - height//2}")
create_grid_layout(root, 1, 2)
# endregion
calculation_window = calculation_window(root, "Расчёт теплопотерь дома", 400, 500)
help_window = help_window(root, "Справка", width, height)
calculate_button = ttk.Button(root, text="Начать расчёт", command=calculation_window.set_calculation_window)
calculate_button.grid(row=0, rowspan=2, ipadx=35, ipady=35)
# region InitializeMenu
main_menu = Menu(root)
main_menu.add_command(label="Справка", command=help_window.set_help_window)
root.config(menu=main_menu)
# endregion
root.mainloop()
