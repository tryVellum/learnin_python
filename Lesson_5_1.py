"""1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка."""

with open("user_data.txt", 'w') as obj_file:
    while True:
        user_line = input('Новая строка: ')
        if user_line == '': break
        obj_file.writelines(user_line + '\n')


