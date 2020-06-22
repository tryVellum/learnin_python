"""6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее."""

from itertools import count, cycle
from sys import argv

_, g, n = argv
g, n = int(g), int(n)
"""
g: True or False, 0 - first iterator (a), 1 - second iterator (b)
n: int
"""

if not g:
    for el in count(n):
        if el > 10:
            break
        else:
            print(el)

if g:
    for el in cycle('ABC'):
        if n == 0: break
        print (el)
        n -= 1
