from tkinter import BooleanVar, StringVar

from enclosures.enclosure import enclosure
from external_thermal_coefficient import external_thermal_coefficient
from thermal_resistance import thermal_resistance


class ceil(enclosure):
    """
    Класс для рассчёта теплопотерь потолка.\n
    При инициализации класса необходимо указать наличие чердака, чтобы учесть внешнюю температуру.\n
    Наследуется от класса `Перекрытие` для унаследования необходимых переменных.
    """

    def __init__(self, ceil_area: StringVar, ceil_thickness: list[StringVar], ceil_material: list[StringVar], has_attic: BooleanVar):
        super().__init__(ceil_area, ceil_thickness, ceil_material)
        self.has_attic = has_attic

    def ceil_thermal_losses(self, internal_temperature: float, external_temperature: float):
        """
        Функция для рассчёта теплопотерь.

        Аргументы:
            internal_temperature: Величина температуры внутри помещения.
            external_temperature: Величина температуры снаружи помещения.
        """

        if self.has_attic.get():
            return float(self.area.get()) * abs(12 - internal_temperature) / thermal_resistance(self.thicknesses, self.materials, external_thermal_coefficient.wall_over_basement.value).calculate_resistance()
        else:
            return float(self.area.get()) * abs(external_temperature - internal_temperature) / thermal_resistance(self.thicknesses, self.materials, external_thermal_coefficient.external_wall.value).calculate_resistance()
