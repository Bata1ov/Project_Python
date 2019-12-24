'''Задача 1
import time
from itertools import cycle
class TraffivLight():
    def __init__(self):
        self.__colors = ['red', 'yellow', 'green']
        self.pool = cycle(self.__colors)

    def running(self):
        self.__color = next(self.pool)
        print(self.__color)
a = TraffivLight()
time_delays = [7, 2, 3]
pool2 = cycle(time_delays)

for i in range(12):
    a.running()
    time.sleep(next(pool2))
print()
'''


'''Задача 2
class Road:
    def __init__(self, lenght=None, width=None):
        self._lenght = lenght
        self._width = width

    def asphalt_calc(self, mass=None, height=None):
        need_asphalt = self._lenght * self._width * mass * height
        print(need_asphalt)


road = Road(20, 5000)

road.asphalt_calc(25, 5)
'''

'''Задача 3
class Worker():

    def __init__(self, name, surname, position, wage, bonus):
        self.name     = name
        self.surname  = surname
        self.position = position
        self.income   = {'wage': wage, 'bonus': bonus}

class position(Worker):

    def get_full_income(self):
        return self.income['wage']+self.income['bonus']

    def get_full_name(self):
        return self.name+' '+self.surname



name, surname, position, wage, bonus = 'Petr','Petrov','Driver',1000,100

W1 = Worker( name, surname, position, wage, bonus)
print(W1.income, W1.name, W1.surname, W1.position)
print()
name, surname, position, wage, bonus = 'Ivan','Pavlov','Plumber',3000,300

P1 = Possision( name, surname, position, wage, bonus)
print(P1.get_full_name(), P1.get_full_income())
print(P1.income, P1.name, P1.surname, P1.posision)
print()
'''

'''Задача 4
class Car:
    def __init__(self, speed, color, name, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self._is_police = is_police

    def go(self):
        print("Машина поехала.")

    def stop(self):
        print("Машина остановилась.")

    def turn(self, direction):
        print(f"Машина повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.speed} км/ч.")


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <= 60:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.\n"
                  f"Превышение скорости. Разрешенная скорость 60 км/ч.")


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed <= 40:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.")
        else:
            print(f"Текущая скорость автомобиля {self.speed} км/ч.\n"
                  f"Превышение скорости. Разрешенная скорость 40 км/ч.")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self._is_police = True

car_dict = {
    "TownCar": TownCar(100, "black", "toyota"),
    "SportCar": SportCar(100, "white", "bmw"),
    "WorkCar": WorkCar(50, "blue", "nissan"),
    "PoliceCar": PoliceCar(200, "yellow", "skoda")
}

for key, value in car_dict.items():
    print(key)
    value.go()
    value.stop()
    value.turn("налево")
    value.show_speed()
    print()
'''

'''Задача 5
class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки ручки {self.title}.")

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки карандаша {self.title}.")

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки маркера {self.title}.")

my_stationery = Stationery("My Stationery")
my_stationery.draw()

my_pen = Pen("My Pen")
my_pen.draw()

my_pencil = Pencil("My Pencil")
my_pencil.draw()

my_handle = Handle("My Handle")
my_handle.draw()
'''