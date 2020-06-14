"""3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369."""

nNumber = input('Введите число n ')

number = int(nNumber * 3) + int(nNumber * 2) + int(nNumber)

print(number)
