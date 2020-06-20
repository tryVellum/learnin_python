"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка."""
from functools import reduce

def my_func(one, two):
    """ one * two

    :param one: int
    :param two: int
    :return: int
    """
    return one * two

my_list = [el for el in range(100, 1001) if not el % 2]
google = reduce(my_func, my_list)
n = 51
for i in range(round(len(str(google)) / n)):
    print(str(google)[n * i:n * (i + 1)])

