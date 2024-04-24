from tkinter import StringVar


class windows():
    """
    Класс для рассчёта теплопотерь окон.\n
    """

    thermal_resistance = {
        "Двойное остекление в спаренных переплетах": 0.4,
        "Двойное остекление в раздельных переплетах": 0.44,
        "Стеклянные блоки": 0.31,
        "Двойное из органического стекла": 0.36,
        "Тройное из органического стекла": 0.52,
        "Тройное остекление в раздельно-спаренных переплетах": 0.55,
        "Однокамерный стеклопакет из стекла обычного": 0.38,
        "Двухкамерный стеклопакет из стекла обычного": 0.51,
        "Обычное стекло и однокамерный стеклопакет в раздельных переплетах из стекла обыного": 0.56,
        "Обычное стекло и двухкамерный стеклопакет в раздельных переплетах из стекла обыного": 0.68,
        "Два однакамерного стеклопакета в сперенных переплетах": 0.7,
        "Два однакамерного стеклопакета в раздельных переплетах": 0.74,
        "Четырехслойное остекление в двух спаренных переплетах": 0.8,
    }

    def __init__(self, window_area: StringVar, window_material: StringVar):
        self.window_area = window_area
        self.window_material = window_material

    def window_thermal_losses(self, internal_temperature: float, external_temperature: float):
        """
        Функция для рассчёта теплопотерь.

        Аргументы:
            internal_temperature: Величина температуры внутри помещения.
            external_temperature: Величина температуры снаружи помещения.
        """

        return float(self.window_area.get()) * abs(external_temperature - internal_temperature) / self.thermal_resistance[self.window_material.get()]
