from tkinter import StringVar


class enclosure():
    """
    Перекрытие является классом, от которого наследуются все остальные классы включенные в помещение.\n
    Содержит в себе переменные площади, списка толщин материалов и списка материалов.
    """

    def __init__(self, area: float, thicknesses: list[StringVar], materials: list[StringVar]):
        self.area = area
        self.thicknesses = thicknesses
        self.materials = materials