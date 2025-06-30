'''
Создание базового класса 'Транспортное средство' и его наследование для создания 
классов 'Автомобиль' и 'Мотоцикл'. В классе 'Транспортное средство' будут 
общие свойства, такие как максимальная скорость и количество колес, а классы
наследники будут иметь свои уникальные свойства и методы.
'''

class Vehicle:
    def __init__(self, max_speed, wheels):
        self.max_speed = max_speed
        self.wheels = wheels

    def info(self):
        return f'Транспортное средство: Максимальная скорость = {self.max_speed} км/ч, Количество колес = {self.wheels}'


class Car(Vehicle):
    def __init__(self, max_speed, doors, body_type):
        super().__init__(max_speed, 4)
        self.doors = doors
        self.body_type = body_type

    def info(self):
        return f'Автомобиль: {super().info()}, Количество дверей = {self.doors}, Тип кузова = {self.body_type}'

    def honk(self):
        return 'Бибип!'

class Motorcycle(Vehicle):
    def __init__(self, max_speed, kind):
        super().__init__(max_speed, 2)  # Все мотоциклы имеют 2 колеса
        self.kind = kind

    def info(self):
        return f'Мотоцикл: {super().info()}, Тип мотоцикла = {self.kind}'

    def wheelie(self):
        return 'Встаю на дыбы!'

car = Car(200, 4, 'Седан')
motorcycle = Motorcycle(250, 'Спортивный')

print(car.info())
print(car.honk())

print(motorcycle.info())
print(motorcycle.wheelie())