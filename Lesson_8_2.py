"""2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
программа должна корректно обработать эту ситуацию и не завершиться с ошибкой."""

class ZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == '__main__':

    inp_dividend, inp_divider = input("Введите делимое число: "), input("Введите делитель: ")

    try:
        inp_divider = int(inp_divider)
        inp_dividend = int(inp_dividend)
        if inp_divider == 0:
            raise ZeroError("Вы ввели 0!")
    except ValueError:
        print("Вы ввели не число")
    except ZeroError as err:
        print(err)
    else:
        print(inp_dividend / inp_divider)

