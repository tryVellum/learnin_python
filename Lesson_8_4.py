"""4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники."""

from abc import ABC


class Warehouse:
    office_equi = {}    # 90
    warehouse_equi= {}  # 10
    defect = {}     # 9999

    def __str__(self):
        return 'Офис' + str(self.office_equi) + '\n'\
               + 'Склад' + str(self.warehouse_equi) + '\n'\
               + 'Склад брака' + str(self.defect)

    def appequi(self, equipment):
        self.warehouse_equi[equipment.name] = equipment.quantity

    def storageArea(self, cls, area: int):
        """ Перемещение на складах 90 -> 10  or 10 -> 90

        :param cls: дочерний класс OfficeEquipment
        :param area: int, перемещение на какой склад по номеру 90 or 10
        :return: None
        """
        if area == 90:
            self.warehouse_equi[cls.name] = self.warehouse_equi[cls.name] - cls.quantity
            try:
                self.office_equi[cls.name] += cls.quantity
            except KeyError:
                self.office_equi[cls.name] = cls.quantity
        elif area == 10:
            self.office_equi[cls.name] = self.office_equi[cls.name] - cls.quantity
            try:
                self.warehouse_equi[cls.name] += cls.quantity
            except KeyError:
                print('Позиция ранее не поступала.')
                self.appequi(cls)
        else:
            print('Неверный код перемещения')

    def defected(self, cls, area: int):
        """ Перемещение в брак со склада 90 or 10

        :param cls: дочерний класс OfficeEquipment
        :param area: int, перемещение на какой склад по номеру 90 or 10
        :return: None
        """
        if area == 90:
            self.office_equi[cls.name] = self.office_equi[cls.name] - cls.quantity
            try:
                self.defect[cls.name] += cls.quantity
            except KeyError:
                self.defect[cls.name] = cls.quantity
        elif area == 10:
            self.warehouse_equi[cls.name] = self.warehouse_equi[cls.name] - cls.quantity
            try:
                self.defect[cls.name] += cls.quantity
            except KeyError:
                self.defect[cls.name] = cls.quantity
        else:
            print('Неверный код перемещения')

class OfficeEquipment(ABC):
    def __init__(self, name: str, quantity: int):
        self.quantity = quantity
        self.name = name
    @property
    def action(self):
        pass


class Calc(OfficeEquipment):
    @property
    def action(self):
        return print('Производит вычисление')


class CashRegister(OfficeEquipment):
    @property
    def action(self):
        return print('Операции с денежными средствами')


class MultifunctionDevice(OfficeEquipment):
    @property
    def action(self):
        return print('Копирует, печатает, сканирует')


if __name__ == '__main__':
    one = Calc('Калькулятор', 233)
    two = CashRegister('Кассовый аппарат', 3)
    three = MultifunctionDevice('МФУ', 10)
    one.action
    two.action
    three.action

    one_defect = Calc('Калькулятор', 5)
    warehouse = Warehouse()
    warehouse.appequi(one)
    warehouse.appequi(two)
    warehouse.appequi(three)
    print(warehouse)
    warehouse.storageArea(one, 90)
    print(warehouse)
    warehouse.defected(one_defect, 90)
    print(warehouse)