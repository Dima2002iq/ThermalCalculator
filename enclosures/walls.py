from tkinter import StringVar

from enclosures.enclosure import enclosure
from thermal_resistance import thermal_resistance
from external_thermal_coefficient import external_thermal_coefficient


class walls(enclosure):
    """
    Класс для рассчёта теплопотерь стен.\n
    Наследуется от класса `Перекрытие` для унаследования необходимых переменных.
    """

    def __init__(self, walls_area: StringVar, wall_thicknesses: list[StringVar], wall_materials: list[StringVar]):
        super().__init__(walls_area, wall_thicknesses, wall_materials)

    def walls_thermal_losses(self, internal_temperature: float, external_temperature: float):
        """
        Функция для рассчёта теплопотерь.

        Аргументы:
            internal_temperature: Величина температуры внутри помещения.
            external_temperature: Величина температуры снаружи помещения.
        """

        return float(self.area.get()) * abs(external_temperature - internal_temperature) / thermal_resistance(self.thicknesses, self.materials, external_thermal_coefficient.external_wall.value).calculate_resistance()
