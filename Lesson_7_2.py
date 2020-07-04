"""2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно."""

from abc import ABC, abstractmethod

class dress(ABC):

    @abstractmethod
    def sum_cloth(self):
        pass

class coat(dress):
    def __init__(self, v :float):
        self.v = v

    @property
    def sum_cloth(self):
        answer = self.v / 6.5 + 0.5
        return round(answer, 3)

class suit(dress):
    def __init__(self, h :float):
        self.h = h

    @property
    def sum_cloth(self):
        answer = self.h * 2 + 0.3
        return answer
