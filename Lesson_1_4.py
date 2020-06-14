"""4. Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции."""

number = input('Введите число: ')
maxNumber = 0
allNumber = []

for num in number:
    allNumber.append(int(num))

i = 0
while i < len(allNumber):
    if allNumber[i] > maxNumber:
        maxNumber = allNumber[i]
    i += 1

print(maxNumber)
