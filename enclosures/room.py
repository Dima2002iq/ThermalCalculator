from tkinter import StringVar


class room():
    """
    Класс для рассчёта инфильтрации.\n
    """

    def __init__(self, room_area: StringVar):
        self.room_area = room_area

    def room_thermal_losses(self, internal_temperature: float, external_temperature: float):
        """
        Функция для рассчёта теплопотерь.

        Аргументы:
            internal_temperature: Величина температуры внутри помещения.
            external_temperature: Величина температуры снаружи помещения.
        """

        return 0.28 * 3 * float(self.room_area.get()) * 1.006 * abs(external_temperature - internal_temperature) * 0.8
