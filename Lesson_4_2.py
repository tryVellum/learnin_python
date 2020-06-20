"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
from random import randint

first_list = [randint(-100, 101) for i in range(20)]
print(first_list)
secont_list = []

for i in range(len(first_list) - 1):
    if first_list[i] < first_list[i + 1]:
        secont_list.append(first_list[i + 1])

therd_list = [first_list[i + 1] for i in range(len(first_list) - 1) if first_list[i] < first_list[i + 1]]

print(secont_list, secont_list == therd_list, therd_list)

