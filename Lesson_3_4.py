"""4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень."""

from fractions import Fraction

def my_func_one(x, y):
    """Возвращает x в степени y.

        Именованные параметры:
        a -- действительное число
        y -- целое отрицательное число

        """

    try:
        c = x ** y
    except:
        c = 0
        return c
    else: return c

def my_func_two(x, y):
    """Возвращает x в отрицательной степени y.

            Именованные параметры:
            a -- действительное число
            y -- целое положительное число

            """
    c = x
    for i in range(1,y):
        c *= x
    try:
        c = 1 / c
    except ZeroDivisionError:
        c = 0
        return c
    else: return c

def valid():
    """:return: действительное число

    С проверкой на не число

    """
    try:
        valid_numb = Fraction(input('Введите любое действительное числочисло (2; 3.14; 0.4; -2/3): '))
    except ValueError:
        return valid()
    else: return valid_numb

a = valid()
while True:
    b = input('Введите целое отрицательное число: -')
    if b.isdigit(): break

b = -(int(b))

print(f'Возведём {a} в отрицательную степень {b}')
print(f'{my_func_two(a, -b)} = {float(my_func_one(a, b))}')
