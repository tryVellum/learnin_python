"""3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров)."""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    def get_full_name(self):
        print(f'{self.surname} {self.name} {self.position}')

    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])


emp_one = Position('Ivan', 'Ivanov', 'STMPT', 25000, 10000)
emp_one.get_full_name()
emp_one.get_total_income()

emp_two = Position('Nina', 'Grigorievna', 'Director', 40000, 20000)
emp_two.get_full_name()
emp_two.get_total_income()