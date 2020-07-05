"""3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка."""


class Onlynumb(Exception):

    def __init__(self, list_el, stop_word):
        self.list_el = list_el
        self.stop_word = stop_word

    @property
    def cheklist(self):
        """Очищает лист от не чисел, с остановкой на стоп слове

        :return: stop_flag:bool, было ли введено стоп столо
                 list_numb:list of float, лист чисел
        """
        list_numb = []
        for i in self.list_el:
            if i == self.stop_word:
                stop_flag = True
                print('Enter stop word')
                break
            else:
                stop_flag = False
            try:
                 list_numb.append('{0:.2f}'.format(float(i)).rstrip('0').rstrip('.'))
            except ValueError:
                print(i, ' is not number or stop word')
                continue
        return stop_flag, list_numb


if __name__ == '__main__':
    list_numbers = []
    while True:
        str_numbers = input('Введите строку чисел через пробел, "stop": ')
        stop_flag, list_numb = Onlynumb(str_numbers.split(), 'stop').cheklist
        for i in list_numb:
            list_numbers.append(i)
        if stop_flag:
            break
        print(list_numbers)

    print(list_numbers)



