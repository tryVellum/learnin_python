"""4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Car {self.name} just left')
    def stop(self):
        print(f'Car {self.name} stopped')
    def turn(self, direction):
        print(f'{self.name} Car turn {direction}')
    def show_speed(self):
        print(f'{self.name} current speed {self.speed} km/h')

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color}-{self.name} please, pull over to the side of the road')
            if not self.is_police:
                print(f'{self.color}-{self.name} is confiscated')
        else:
            print(f'{self.name} current speed {self.speed} km/h')
class SportCar(Car):
    pass
class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color}-{self.name} please, pull over to the side of the road')
            if not self.is_police:
                print(f'{self.color}-{self.name} is confiscated')
        else:
            print(f'{self.name} current speed {self.speed} km/h')

class PoliceCar(Car):
    pass

car_one = TownCar(70, 'White', 'Lada', True)
car_two = SportCar(250, 'Red', 'BMV', 0)
car_three = WorkCar(30, 'Black', 'Opel', False)
car_four = PoliceCar(120, 'White-Blue', 'Volkswagen', True)

car_one.go()
car_two.go()
car_three.go()
car_four.go()
print('')
car_one.turn('left')
car_two.turn('right')
car_three.turn('straight')
car_four.turn('back')
print('')
car_one.show_speed()
car_two.show_speed()
car_three.show_speed()
car_four.show_speed()
print('')
car_one.stop()
car_two.stop()
car_three.stop()
car_four.stop()