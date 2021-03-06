# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
# пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это
# могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothing:
    def __init__(self, v, h):
        self.volume = v
        self.height = h

    @abstractmethod
    def coat_c(self):
        return self.volume / 6.5 + 0.5

    @abstractmethod
    def suit_c(self):
        return self.height * 2 + 0.3

    @property
    def common_c(self):
        return print(f" Общий расход ткани составляет: \n {((self.volume / 6.5 + 0.5) + (self.height * 2 + 0.3))}")

class Coat(Clothing):
    def __init__(self, v, h):
        super().__init__(v, h)
    def coat_c(self):
        return self.volume / 6.5 + 0.5

class Suit(Clothing):
    def __init__(self, v, h):
        super().__init__(v, h)
    def suit_c(self):
        return self.height * 2 + 0.3


coat = Coat(5, 5)
print(coat.coat_c())
suit = Suit(7, 10)
print(suit.suit_c())
clothing = Clothing(20, 30)
print(clothing.common_c)