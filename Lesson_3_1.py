"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def calculator(a, b):
    """Выполняет деление a на b, с проверкой деление на 0

    :param a: int
    :param b: int
    :return: int
    """
    try:
        c = a / b
    except ZeroDivisionError:
        print('WARNING: Ноль можно разделить на любое число, не равное нулю.'
              'При этом значение такой дроби будет 0, а деление на ноль запрещено')
        c = "Поделился на ноль"
        return c

    else: return round(c, 3) # в задании не указано, но выведем результат


while True:
    number_one = input('Первое число: ')
    if number_one.isdigit(): break
while True:
    number_two = input('Второе число: ')
    if number_two.isdigit(): break

print(f'Ответ: {calculator(int(number_one), int(number_two))}')

