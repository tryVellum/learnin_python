"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его
нарушении выводить соответствующее сообщение и завершать скрипт."""

import time
import sys

def time_count(t):
    print(f'Осталось времени: {t}')
    t -= 1
    time.sleep(1)
    if t == -1: return
    time_count(t)

class TrafficLight:
    def __init__(self, _color):
        if _color == 'Красный':
            self._color = _color
        else:
            print('Скрипт завершен')
            sys.exit()

    def running(self):
        TrafficLight._color = 'Красный'
        print(f'\033[91m{TrafficLight._color}\033[0m')
        time_count(7)
        TrafficLight._color = 'Желтый'
        print(f'\033[93m{TrafficLight._color}\033[0m')
        time_count(2)
        TrafficLight._color = 'Зелёный'
        print(f'\033[92m{TrafficLight._color}\033[0m')
        time_count(5)

traffic = TrafficLight('Красный')
traffic.running()

traffic_two = TrafficLight('H')
traffic.running()

traffic = TrafficLight('Красный')
traffic.running()