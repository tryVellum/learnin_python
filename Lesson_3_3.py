'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.'''

def my_func(a, b ,c):
    sumtwo = a + b + c - min([a, b, c])
    return sumtwo

while True:
    number_one = input('Первое число: ')
    if number_one.isdigit(): break
while True:
    number_two = input('Второе число: ')
    if number_two.isdigit(): break
while True:
    number_thr = input('Третье число: ')
    if number_thr.isdigit(): break

print(my_func(int(number_one), int(number_two), int(number_thr)))