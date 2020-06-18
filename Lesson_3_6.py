"""6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием.
В программу должна попадать строка из слов, разделенных пробелом.
Каждое слово состоит из латинских букв в нижнем регистре.
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
Необходимо использовать написанную ранее функцию int_func()."""

def int_func(word):
    """(‘text’) -> Text

    :param word: str, одно слово
    :return: str, одно слово, первая заглавная
    """
    word = word.lower()
    word = word.title()
    return word

user_str = input("Введите строку: ")
user_list = user_str.split()
new_list = []
for word in user_list:
    new_list.append(int_func(word))

new_str = ' '.join(new_list)
print(new_str)


