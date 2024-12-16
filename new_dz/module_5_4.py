# Работа __new__:
# 'data' передаётся (упаковывается) в *args, т.к. это позиционный аргумент.
# Он будет находиться под индексом 0 как единственный элемент кортежа.
# second=25 и third=3.14 передаются (упаковываются) в **kwargs т.к. это именованные аргументы.
# Они будут находиться под ключами 'second' и 'third' со значением 25 и 3.14 соответственно в словаре.
# Передача данных из __new__ в __init__:
# После того как метод __new__ отработает до конца, произойдут следующие события с параметрами __init__:
# В параметр first распакуется из args единственный аргумент 'data'.
# В параметр second распакуется значение под ключом с тем же названием из словаря kwargs.
# В параметр third распакуется значение под ключом с тем же названием из словаря kwargs.
                        # Задача "История строительства":
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта,
# тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
# Название объекта добавлялось в список cls.houses_history.
# Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__,
# а также значение атрибута houses_history.
# Пример выполнения программы:        # Вывод на консоль:
# h1 = House('ЖК Эльбрус', 10)                           # ['ЖК Эльбрус']
# print(House.houses_history)                            # ['ЖК Эльбрус', 'ЖК Акация']
# h2 = House('ЖК Акация', 20)                            # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# print(House.houses_history)                            # ЖК Акация снесён, но он останется в истории
# h3 = House('ЖК Матрёшки', 20)                          # ЖК Матрёшки снесён, но он останется в истории
# print(House.houses_history)                            # ['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
# # Удаление объектов                                    ЖК Эльбрус снесён, но он останется в истории
# del h2
# del h3                        Примечания: Более подробно о работе метода __new__ можно узнать здесь.
# print(House.houses_history)               В методе __new__ можно обращаться к атрибутам текущего класса при помощи параметра cls.

class House:
    "класс для домов"
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name: str, number_of_floors: int):
        if not isinstance(number_of_floors, int):
            raise TypeError('numberOfFloors должен быть целым числом')
        if not isinstance(name, str):
            raise TypeError('buildingType должен быть строкой')
        self.name = name
        self.number_of_floors = number_of_floors
        self.__str__()

    def __del__(self):
        return print(f"{self.name} снесён, но он останется в истории")

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __radd__(self, other):
        if not isinstance(other, int):
            raise AssertionError('Правый операнд должкн быть int')
        return House(self.name, self.number_of_floors + other)

    def __add__(self, other):
        if not isinstance(other, int):
            raise AssertionError('Правый операнд должкн быть int')
        return House(self.name, self.number_of_floors + other)

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f"Название: {self.name}, кол-во этажей: {self.number_of_floors}")


    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print(f"Такого этажа в {self.name} не существует")
        else:
            for i in range(1, self.new_floor + 1):
                print(f'{self.name}, едем, этаж {i}')


# h1 = House('qwe', 34)
# print(h1)
# print(House.houses_history)
# h2 = House('asd', 23)
# print(h2)
# print(House.houses_history)

h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
# Удаление объектов
del h2
del h3
print(House.houses_history)
