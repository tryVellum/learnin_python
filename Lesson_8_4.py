"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""

from abc import ABC


class Warehouse:
    office_equi = {}

    def __str__(self):
        return str(self.office_equi)

    def appequi(self, equipment):
        self.office_equi[equipment.name] = equipment.inv_num


class OfficeEquipment(ABC):
    def __init__(self, name, inv_num):
        self.inv_num = inv_num
        self.name = name
    @property
    def action(self):
        pass


class Calc(OfficeEquipment):
    @property
    def action(self):
        print('Производит вычисление')


class CashRegister(OfficeEquipment):
    @property
    def action(self):
        print('Операции с денежными средствами')


class MultifunctionDevice(OfficeEquipment):
    @property
    def action(self):
        print('Копирует, печатает, сканирует')


if __name__ == '__main__':
    one = Calc('Калькулятор', 233)
    two = CashRegister('Кассовый аппарат', 145)
    three = MultifunctionDevice('МФУ', 110)
    one.action
    two.action
    three.action

    warehouse = Warehouse()
    warehouse.appequi(one)
    warehouse.appequi(two)
    warehouse.appequi(three)
    print(warehouse)
