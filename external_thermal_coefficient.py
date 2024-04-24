import enum


class external_thermal_coefficient(enum.Enum):
    """
    Класс для хранения коэффициентов теплопроводности для различных типов стен.\n
    """

    external_wall = 23
    wall_over_cold_basement = 17
    wall_over_basement = 12
