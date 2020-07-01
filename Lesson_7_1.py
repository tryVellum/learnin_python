"""1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы."""

import random

class Matrix:
    def __init__(self, list_list:list):
        self.list_list = list_list

    def __str__(self):
        for i in self.list_list:
            print(i)
        return ''

    def __add__(self, other):
        new_marix = []
        for i in range(len(self.list_list)):
            new_list = []
            for j in range(len(self.list_list[i])):
                ii = self.list_list[i]
                try:
                    jj = other.list_list[i]
                    new_list.append(ii[j] + jj[j])
                except IndexError:
                    new_list.append(ii[j])
            new_marix.append(new_list)
        return Matrix (new_marix)

def generate_matrix(a=1, b=1):
    """Генератор cлучайного списка списков
    
    :param a: int, количество списков
    :param b: int, количество елементов в списке
    :return: list, матрица
    """
    matrix_list = [[random.randint(0, 50) for i in range(b)] for i in range(a)]
    return matrix_list

one = Matrix(generate_matrix(4, 4))
print(one)
two = Matrix(generate_matrix(3, 3))
print(two)
print(one + two)
