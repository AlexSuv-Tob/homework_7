'''
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определенное название.
 К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды
 существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть
 обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные
на этом уроке знания: реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.
'''
from abc import ABC, abstractmethod

class Clothes:
    def __init__(self, v, h):
        self.v = v
        self.h = h
        self.res = v/(6.5 + 0.5) + (2 * h + 0.3)

    @abstractmethod
    def exp_c(self, v):
        pass

    @abstractmethod
    def exp_sint(self, h):
        pass

    @property
    def my_class(self):
        return f' введенный размер пальто {self.v}, ' \
               f'введенный размер костюма {self.h}'

class Coat(Clothes):
    def exp_c(self, v):
        return v / 6.5 + 0.5

class Suit(Clothes):
    def exp_s(self, h):
        return 2 * h + 0.3

cl = Clothes(32, 35)
co = Coat(32, 35)
su = Suit(32, 35)
print(co.exp_c(32))
print(su.exp_s(35))
print(cl.res)
print(cl.my_class)





