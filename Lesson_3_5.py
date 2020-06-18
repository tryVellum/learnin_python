"""5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""


sum_numbers = 0
stop = False
while True:
    str_numbers = input('Введите строку чисел через пробел, стоп символ "s": ')
    list_numbers = str_numbers.split()
    for i in list_numbers:
        if i == 's':
            stop = True
            break
        try:
            sum_numbers += float(i)
        except ValueError:
            continue
    print(sum_numbers)
    if stop: break
if float.is_integer(sum_numbers):
    print(int(sum_numbers))
else:
    print(sum_numbers)
