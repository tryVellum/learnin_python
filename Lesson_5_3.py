"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников."""

file_sum = 0
with open('file_5_3', 'r') as data:
    lines = len(data.readlines())
    data.seek(0)
    for i in range(lines):
        famyle, salary = data.readline().split()
        file_sum += int(salary)
        if int(salary) < 20000: print(f'Получает меньше МРОТа: {famyle}')

print(f'Средняя величина дохода сотрудников: {file_sum/lines}')