# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} go'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} changed direction'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is acceptable for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed for that car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than it is accepted for that car'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


mercedes = SportCar(150, 'Silver', 'Mercedes', False)
moskvich = TownCar(40, 'White', 'Moskvich', False)
lada = WorkCar(70, 'Brown', 'Lada', False)
citroen = PoliceCar(120, 'White-Blue', 'Citroen', True)
print(lada.turn_left())
print(f'When {moskvich.turn_right()}, then {mercedes.stop()}')
print(f'{lada.name} is {lada.color}')
print(f'Is {mercedes.name} a police car? {mercedes.is_police}')
print(f'Is {lada.name} a police car? {lada.is_police}')
print(mercedes.show_speed())
print(moskvich.show_speed())
print(citroen.police())
print(citroen.show_speed())