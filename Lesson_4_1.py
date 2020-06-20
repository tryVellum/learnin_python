"""1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

def calc_salary(worck_shift = 0, hour = 0, money_hour = 0, bonus = 0):
    """Расчета заработной платы сотрудника

    :param worck_shift: int, отработанные смены
    :param hour: int, колличество часов в семене
    :param money_hour: int, руб./час
    :param bonus: int, премия
    :return: float, расчет заработной платы
    """
    salary = (worck_shift * hour * money_hour) * 0.86 + bonus
    return salary


_, *inf = argv
shift_data = [float(i) for i in inf]
print("Зарплата составит:", calc_salary(*shift_data))
