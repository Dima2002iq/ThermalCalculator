from tkinter import BooleanVar, StringVar

from enclosures.enclosure import enclosure
from external_thermal_coefficient import external_thermal_coefficient
from thermal_resistance import thermal_resistance


class floor(enclosure):
    """
    Класс для рассчёта теплопотерь пола.\n
    При инициализации класса необходимо указать наличие подвала, чтобы учесть внешнюю температуру.\n
    Наследуется от класса `Перекрытие` для унаследования необходимых переменных.
    """

    def __init__(self, floor_area: StringVar, floor_thickness: list[StringVar], floor_material: list[StringVar], has_basement: BooleanVar):
        super().__init__(floor_area, floor_thickness, floor_material)
        self.has_basement = has_basement

    def floor_thermal_losses(self, internal_temperature: float, external_temperature: float):
        """
        Функция для рассчёта теплопотерь.

        Аргументы:
            internal_temperature: Величина температуры внутри помещения.
            external_temperature: Величина температуры снаружи помещения.
        """

        if self.has_basement.get():
            return float(self.area.get()) * abs(5 - internal_temperature) / thermal_resistance(self.thicknesses, self.materials, external_thermal_coefficient.wall_over_basement.value).calculate_resistance()
        else:
            return float(self.area.get()) * abs(external_temperature - internal_temperature) / thermal_resistance(self.thicknesses, self.materials, external_thermal_coefficient.external_wall.value).calculate_resistance()
