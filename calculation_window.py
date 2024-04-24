from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from grid_layout import create_grid_layout
from thermal_resistance import thermal_resistance
from window import window
from enclosures.walls import walls
from enclosures.room import room
from enclosures.floor import floor
from enclosures.ceil import ceil
from enclosures.windows import windows


class calculation_window(window):
    """
    Класс, который создает окно пользователя для ввода и рассчёта теплопотерь.\n
    Наследует класс `window`, чтобы использовать его методы.
    """

    current_tab = None
    walls = None
    infiltration = None
    floor = None
    bool_basement = None
    basement_walls = None
    basement_floor = None
    ceil = None
    bool_attic = None
    attic_walls = None
    attic_ceil = None
    windows = None
    heating_season = None
    external_temperature = None
    internal_temperature = None

    def set_calculation_window(self):
        """
        Функция, создающая окно пользовательского ввода и привязывающая переменные класса к полям ввода.
        """

        self.create_new_window()
        notebook = ttk.Notebook(self.window)
        notebook.pack(expand=True, fill=BOTH)

        items = ["Общее", "Стены", "Инфильтрация", "Пол", "Потолок", "Окна"]

        for item in items:
            frame = ttk.Frame(notebook)
            frame.pack(expand=True, fill=BOTH)
            notebook.add(frame, text=item)

        # region General
        ttk.Label(notebook.children["!frame"],
                  text="Количество дней отопительного сезона").pack()
        self.heating_season = StringVar(notebook.children["!frame"], 225)
        ttk.Entry(notebook.children["!frame"],
                  textvariable=self.heating_season).pack(pady=5)
        ttk.Label(notebook.children["!frame"],
                  text="Средняя температура самой холодной пятидневки в году, °C").pack()
        self.external_temperature = StringVar(
            notebook.children["!frame"], -35.0)
        ttk.Entry(notebook.children["!frame"],
                  textvariable=self.external_temperature).pack(pady=5)
        ttk.Label(notebook.children["!frame"],
                  text="Температура внутри помещения, °C").pack()
        self.internal_temperature = StringVar(
            notebook.children["!frame"], 21.0)
        ttk.Entry(notebook.children["!frame"],
                  textvariable=self.internal_temperature).pack(pady=5)
        ttk.Button(
            notebook.children["!frame"],
            text="Далее",
            command=lambda: self.select_next_tab(notebook)
        ).pack(anchor="se", padx=10, pady=10, side="right")
        # endregion
        # region Walls
        self.walls = walls(StringVar(), [], [])
        self.set_entry(
            notebook.children["!frame2"],
            "Площадь стен, м²",
            self.walls.area
        )
        ttk.Label(notebook.children["!frame2"], text="Материалы слоёв").pack()
        material_frame = ttk.Frame(
            notebook.children["!frame2"], borderwidth=1, relief=SOLID, padding=[8, 5])
        self.add_layer(
            material_frame,
            self.walls.thicknesses,
            self.walls.materials
        )
        material_frame.pack()
        ttk.Button(
            notebook.children["!frame2"],
            text="Далее",
            command=lambda: self.select_next_tab(notebook)
        ).pack(anchor="se", padx=10, pady=10, side="right")
        ttk.Button(
            notebook.children["!frame2"],
            text="Назад",
            command=lambda: self.select_previous_tab(notebook)
        ).pack(anchor="sw", padx=10, pady=10, side="left")
        # endregion
        # region Infiltration
        self.infiltration = room(StringVar())
        self.set_entry(
            notebook.children["!frame3"],
            "Площадь жилого помещения, м²",
            self.infiltration.room_area
        )
        ttk.Button(
            notebook.children["!frame3"],
            text="Далее",
            command=lambda: self.select_next_tab(notebook)
        ).pack(anchor="se", padx=10, pady=10, side="right")
        ttk.Button(
            notebook.children["!frame3"],
            text="Назад",
            command=lambda: self.select_previous_tab(notebook)
        ).pack(anchor="sw", padx=10, pady=10, side="left")
        # endregion
        # region Floor
        self.bool_basement = BooleanVar(notebook.children["!frame4"])
        self.floor = floor(StringVar(), [], [], self.bool_basement)
        self.basement_walls = walls(StringVar(), [], [])
        self.basement_floor = floor(
            StringVar(), [], [], BooleanVar(value=False))
        self.set_entry(
            notebook.children["!frame4"],
            "Площадь пола, м²",
            self.floor.area
        )
        ttk.Label(notebook.children["!frame4"], text="Материалы слоёв").pack()
        material_frame = ttk.Frame(
            notebook.children["!frame4"], borderwidth=1, relief=SOLID, padding=[8, 5])
        self.add_layer(
            material_frame,
            self.floor.thicknesses,
            self.floor.materials
        )
        material_frame.pack()
        Checkbutton(
            notebook.children["!frame4"],
            text="Наличие подвала",
            variable=self.bool_basement,
            command=lambda: self.check_changed(
                self.bool_basement,
                notebook.children["!frame4"],
                ["Площадь стен подвала, м²", "Площадь пола подвала, м²"],
                [self.basement_walls.area, self.basement_floor.area],
                [self.basement_walls.thicknesses, self.basement_floor.thicknesses],
                [self.basement_floor.materials, self.basement_walls.materials]
            )
        ).pack()
        ttk.Button(
            notebook.children["!frame4"],
            text="Далее",
            command=lambda: self.select_next_tab(notebook)
        ).pack(anchor="se", padx=10, pady=10, side="right")
        ttk.Button(
            notebook.children["!frame4"],
            text="Назад",
            command=lambda: self.select_previous_tab(notebook)
        ).pack(anchor="sw", padx=10, pady=10, side="left")
        # endregion
        # region Ceiling
        self.bool_attic = BooleanVar(notebook.children["!frame5"])
        self.ceil = ceil(StringVar(), [], [], self.bool_attic)
        self.attic_walls = walls(StringVar(), [], [])
        self.attic_ceil = ceil(StringVar(), [], [], BooleanVar(value=False))
        self.set_entry(
            notebook.children["!frame5"],
            "Площадь потолка, м²",
            self.ceil.area,
        )
        ttk.Label(notebook.children["!frame5"], text="Материалы слоёв").pack()
        material_frame = ttk.Frame(
            notebook.children["!frame5"], borderwidth=1, relief=SOLID, padding=[8, 5])
        self.add_layer(
            material_frame,
            self.ceil.thicknesses,
            self.ceil.materials
        )
        material_frame.pack()
        Checkbutton(
            notebook.children["!frame5"],
            text="Наличие чердака",
            variable=self.bool_attic,
            command=lambda: self.check_changed(
                self.bool_attic,
                notebook.children["!frame5"],
                ["Площадь стен чердака, м²", "Площадь потолка на чердаке, м²"],
                [self.attic_walls.area, self.attic_ceil.area],
                [self.attic_walls.thicknesses, self.attic_ceil.thicknesses],
                [self.attic_ceil.materials, self.attic_walls.materials]
            )
        ).pack()
        ttk.Button(
            notebook.children["!frame5"],
            text="Далее",
            command=lambda: self.select_next_tab(notebook)
        ).pack(anchor="se", padx=10, pady=10, side="right")
        ttk.Button(
            notebook.children["!frame5"],
            text="Назад",
            command=lambda: self.select_previous_tab(notebook)
        ).pack(anchor="sw", padx=10, pady=10, side="left")
        # endregion
        # region Windows
        self.windows = windows(StringVar(), StringVar())
        self.set_entry(
            notebook.children["!frame6"],
            "Площадь остекления, м²",
            self.windows.window_area
        )
        ttk.Label(notebook.children["!frame6"],
                  text="Материал остекления").pack()
        ttk.Combobox(notebook.children["!frame6"], values=list(
            windows.thermal_resistance.keys()), textvariable=self.windows.window_material).pack()
        ttk.Button(
            notebook.children["!frame6"],
            text="Рассчитать",
            command=self.calculate
        ).pack(anchor="se", padx=10, pady=10, side="right")
        ttk.Button(
            notebook.children["!frame6"],
            text="Назад",
            command=lambda: self.select_previous_tab(notebook)
        ).pack(anchor="sw", padx=10, pady=10, side="left")
        # endregion

    def set_entry(self, root, entry, text_variable):
        """
        Создает пару метки и поля ввода.

        Аргументы:
            root: родительский виджет, в который будут добавлены виджеты.
            entry: текст метки.
            text_variable: переменная, к которой будет привязано поле ввода.
        """

        ttk.Label(root, text=entry).pack()
        ttk.Entry(root, textvariable=text_variable).pack(pady=5)

    def add_layer(self, root, thickness_variables: list[StringVar], material_variables: list[StringVar]):
        """
        Добавляет дополнительные поля ввода для толщины и слоя.\n

        Аргументы:
            root: родительский виджет, в который будут добавлены виджеты.
            thickness_variables: список переменных для привязки толщины слоя.
            material_variables: список переменных для привязки материала слоя.
        """

        material_variables.append(StringVar())
        thickness_variables.append(StringVar())
        for widget in root.winfo_children():
            if widget.winfo_class() == "TButton":
                widget.destroy()
        create_grid_layout(root, 2, len(material_variables) * 2 + 1)
        ttk.Label(root, text="Толщина слоя, м").grid(
            row=len(material_variables) * 2 - 2, column=0, pady=5)
        ttk.Entry(root, textvariable=thickness_variables[-1]).grid(
            row=len(material_variables) * 2 - 2, column=1, pady=5)
        ttk.Label(root, text="Материал слоя").grid(
            row=len(material_variables) * 2 - 1, column=0)
        ttk.Combobox(root, values=list(thermal_resistance.thermal_conduction.keys(
        )), textvariable=material_variables[-1]).grid(row=len(material_variables) * 2 - 1, column=1)
        ttk.Button(root, text="Удалить слой", command=lambda: self.remove_layer(
            root, thickness_variables, material_variables)).grid(row=len(material_variables) * 2, column=0, pady=5)
        ttk.Button(root, text="Добавить слой", command=lambda: self.add_layer(
            root, thickness_variables, material_variables)).grid(row=len(material_variables) * 2, column=1, pady=5)

    def remove_layer(self, root, thickness_variables: list[StringVar], material_variables: list[StringVar]):
        """
        Удаляет последний слой.

        Аргументы:
            root: родительский виджет, в котором будут удалены виджеты.
            thickness_variables: список переменных для привязки толщины слоя.
            material_variables: список переменных для привязки материала слоя.
        """

        if len(thickness_variables) > 1 and len(material_variables) > 1:
            thickness_variables.pop()
            material_variables.pop()
            for widget in root.winfo_children()[-6:]:
                widget.destroy()
            create_grid_layout(root, 2, len(material_variables) * 2 + 1)
            ttk.Button(root, text="Удалить слой", command=lambda: self.remove_layer(
                root, thickness_variables, material_variables)).grid(row=len(material_variables) * 2, column=0, pady=5)
            ttk.Button(root, text="Добавить слой", command=lambda: self.add_layer(
                root, thickness_variables, material_variables)).grid(row=len(material_variables) * 2, column=1, pady=5)

    def select_next_tab(self, notebook):
        """
        Переключает на следующую вкладку.

        Аргументы:
            notebook: виджет вкладок, на котором будет произведена операция.
        """

        current_tab = notebook.index(notebook.select())
        notebook.select(current_tab + 1)

    def select_previous_tab(self, notebook):
        """
        Переключает на предыдущую вкладку.

        Аргументы:
            notebook: виджет вкладок, на котором будет произведена операция.
        """

        current_tab = notebook.index(notebook.select())
        notebook.select(current_tab - 1)

    def check_changed(self, bool_variable, root, entries, text_variables, thikness_variables, material_variables):
        """
        Проверяет изменение значения чекбокса и добавляет или удаляет поля ввода.

        Аргументы:
            bool_variable: переменная, привязанная к чекбоксу.
            root: родительский виджет, в который будут добавлены или удалены виджеты.
            entries: список текстов меток.
            text_variables: список переменных для привязки полей ввода.
            thikness_variables: список переменных для привязки толщины слоя.
            material_variables: список переменных для привязки материала слоя.
        """

        if bool_variable.get():
            additional_frame = ttk.Frame(
                root, borderwidth=1, relief=SOLID, padding=[8, 5])
            self.set_entry(additional_frame, entries[0], text_variables[0])
            material_frame = ttk.Frame(
                additional_frame, borderwidth=1, relief=SOLID, padding=[8, 5])
            ttk.Label(additional_frame, text="Материалы слоёв").pack()
            self.add_layer(
                material_frame, thikness_variables[0], material_variables[0])
            material_frame.pack()
            additional_frame.pack(side="left")
            additional_frame = ttk.Frame(
                root, borderwidth=1, relief=SOLID, padding=[8, 5])
            self.set_entry(additional_frame, entries[1], text_variables[1])
            material_frame = ttk.Frame(
                additional_frame, borderwidth=1, relief=SOLID, padding=[8, 5])
            ttk.Label(additional_frame, text="Материалы слоёв").pack()
            self.add_layer(
                material_frame, thikness_variables[1], material_variables[1])
            material_frame.pack()
            additional_frame.pack(side="right")
        else:
            for widget in root.winfo_children()[-2:]:
                widget.destroy()

    def calculate(self):
        """
        Функция для рассчёта теплопотерь и объёма сжигаемого газа.
        """

        if not True:
            print(f"Qстен = {self.walls.walls_thermal_losses()},")
            print(f"Qинф = {self.infiltration.room_thermal_losses()},")
            print(f"Qпол = {self.floor.floor_thermal_losses()},")
            print(f"Qпот = {self.ceil.ceil_thermal_losses()},")
            print(f"Qокн = {self.windows.window_thermal_losses()},")
            if self.bool_basement.get():
                print(
                    f"Qподв = {self.basement_walls.walls_thermal_losses() + self.basement_floor.floor_thermal_losses()}")
            if self.bool_attic.get():
                print(
                    f"Qчерд = {self.attic_walls.walls_thermal_losses() + self.attic_ceil.ceil_thermal_losses()}")
        try:
            thermal_losses = self.walls.walls_thermal_losses(float(self.internal_temperature.get()), float(self.external_temperature.get())) \
                + self.infiltration.room_thermal_losses(float(self.internal_temperature.get()), float(self.external_temperature.get())) \
                + self.floor.floor_thermal_losses(float(self.internal_temperature.get()), float(self.external_temperature.get())) \
                + self.ceil.ceil_thermal_losses(float(self.internal_temperature.get()), float(self.external_temperature.get())) \
                + self.windows.window_thermal_losses(
                    float(self.internal_temperature.get()), float(self.external_temperature.get()))
        except:
            showerror(
                "Ошибка", "Неправильно внесены значения в поля ввода! Проверьте поля ввода на корректность значений.")
        if self.bool_basement.get():
            thermal_losses += self.basement_walls.walls_thermal_losses() + \
                self.basement_floor.floor_thermal_losses()
        if self.bool_attic.get():
            thermal_losses += self.attic_walls.walls_thermal_losses() + \
                self.attic_ceil.ceil_thermal_losses()
        burned_gas_volume = thermal_losses * 1.15 / (12600 * 0.95)
        showinfo("Результат",
                 f"\
Теплопотери составляют: {thermal_losses:.2f} Вт\n\
Объём сжигаемого газа составляет: {burned_gas_volume:.2f} м³/ч\n\
За весь отопительный сезон будет израсходовано {burned_gas_volume * 24 * int(self.heating_season.get()):.2f} м³ газа\
"
                 )
