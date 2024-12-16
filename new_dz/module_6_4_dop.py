# Атрибуты класса Figure: sides_count = 0
# Каждый объект класса Figure должен обладать следующими атрибутами:
# Атрибуты(инкапсулированные): __sides(список сторон (целые числа)), __color(список цветов в формате RGB)
# Атрибуты(публичные): filled(закрашенный, bool)
# И методами:
# Метод get_color, возвращает список RGB цветов.
# Метод __is_valid_color - служебный, принимает параметры r, g, b, который проверяет корректность переданных значений
# перед установкой нового цвета. Корректным цвет: все значения r, g и b - целые числа в диапазоне от 0 до 255 (включительно).
# Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения,
# предварительно проверив их на корректность. Если введены некорректные данные, то цвет остаётся прежним.
#       Метод __is_valid_sides - служебный, принимает неограниченное кол-во сторон, возвращает True если все стороны целые
# положительные числа и кол-во новых сторон совпадает с текущим, False - во всех остальных случаях.
# Метод get_sides должен возвращать значение я атрибута __sides.
#       Метод __len__ должен возвращать периметр фигуры.
# Метод set_sides(self, *new_sides) должен принимать новые стороны, если их количество не равно sides_count,
# то не изменять, в противном случае - менять.
# Атрибуты класса Circle: sides_count = 1
# Каждый объект класса Circle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Атрибут __radius, рассчитать исходя из длины окружности (одной единственной стороны).
# Метод get_square возвращает площадь круга (можно рассчитать как через длину, так и через радиус).
# Атрибуты класса Triangle: sides_count = 3
# Каждый объект класса Triangle должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure
# Метод get_square возвращает площадь треугольника. (можно рассчитать по формуле Герона)
# Атрибуты класса Cube: sides_count = 12
# Каждый объект класса Cube должен обладать следующими атрибутами и методами:
# Все атрибуты и методы класса Figure.
# Переопределить __sides сделав список из 12 одинаковы сторон (передаётся 1 сторона)
# Метод get_volume, возвращает объём куба.
# ВАЖНО!
# При создании объектов делайте проверку на количество переданных сторон, если сторон не ровно sides_count,
# то создать массив с единичными сторонами и в том кол-ве, которое требует фигура.
# Пример 1: Circle((200, 200, 100), 10, 15, 6), т.к. сторона у круга всего 1, то его стороны будут - [1]
# Пример 2: Triangle((200, 200, 100), 10, 6), т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
# Пример 3: Cube((200, 200, 100), 9), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [9, 9, 9, ....., 9] (12)
# Пример 4: Cube((200, 200, 100), 9, 12), т.к. сторон(рёбер) у куба - 12, то его стороны будут - [1, 1, 1, ....., 1]
# Примечания (рекомендации):
# Рекомендуется сделать дополнительные (свои проверки) работы методов объектов каждого класса.
# Делайте каждый класс и метод последовательно и проверяйте работу каждой части отдельно.
# Для проверки принадлежности к типу рекомендуется использовать функцию isinstance.
# Помните, служебные инкапсулированные методы можно и нужно использовать только внутри текущего класса.
# Вам не запрещается вводить дополнительные атрибуты и методы, творите, но не переборщите!

from math import pi as p

class Figure:
    sides_count = 0

    def __init__(self,  color, *sides, filled=False):
        if len(sides) == 1:
            self.__sides = list(sides) * self.sides_count
        elif len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        elif len(sides) == self.sides_count:
            self.__sides = list(sides)
        self.__color = list(color)
        self.filled = filled

    def get_sides(self):
        return self.__sides

    def get_color(self):
        return self.__color

    def __is_valid_color(self, R, G, B):
       return 0 <= R <= 255 and 0 <= G <= 255 and 0 <= B <= 255

    def set_color(self, R, G, B):
        if self.__is_valid_color(R, G, B):
            self.__color = [R, G, B]

    def __len__(self):
        return sum(self.__sides)

    def __is_valid_sides(self, *sides):
        return all(isinstance(x, int) and x > 0 for x in sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        elif len(new_sides) == 1 and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides) * self.sides_count

class Circle(Figure):
    sides_count = 1

    def radius(self):

        __radius = self._Figure__sides[0] / 6.283
        return __radius

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)

    def get_square(self):
        radius = self.radius()
        return round(3.1415 * radius ** 2, 3)

class Triangle(Figure):
    sides_count = 3

    def set_sides(self, *new_sides):
        super().set_sides(*new_sides)

    def get_square(self):
        from math import sqrt
        p = sum(self._Figure__sides) / 2
        return round(sqrt((p * (p - self._Figure__sides[0]) * (p - self._Figure__sides[1]) * (p - self._Figure__sides[2]))), 3)

class Cube(Figure):
    sides_count = 12

    def get_volume(self):
        return round(self._Figure__sides[0] ** 3, 3)

circle1 = Circle((200, 200, 100), 10)
triangle1 = Triangle((100, 150, 200), 3, 4, 5)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())
triangle1.set_color(200,100,200) # изменится
print(triangle1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
triangle1.set_sides(7) # изменится
print(triangle1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(len(triangle1))
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
print(circle1.get_square())
print(triangle1.get_square())
