"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран."""

import random

num_sum = 0
with open('file_5_5.txt', 'w+') as numbers:
    for i in range(random.randint(1, 100)):
        numbers.write(str(round(random.random() * 1000, 3)) + ' ')
    numbers.seek(0)
    numbers_str = numbers.read().split()
    for i in numbers_str:
        num_sum += float(i)

print(num_sum)
