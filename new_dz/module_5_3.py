# Необходимо дополнить класс House следующими специальными методами:
# __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
# Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
# результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
# __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
# __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
# Остальные методы арифметических операторов, где self - x, other - y:
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
# Пример выполняемого кода:                                                 # Вывод на консоль:
# h1 = House('ЖК Эльбрус', 10)                                              # Название: ЖК Эльбрус, кол-во этажей: 10
# h2 = House('ЖК Акация', 20)                                               # Название: ЖК Акация, кол-во этажей: 20
# print(h1)                                                                 # False
# print(h2)                                                                 # Название: ЖК Эльбрус, кол-во этажей: 20
# print(h1 == h2) # __eq__                                                  # True
# h1 = h1 + 10 # __add__                                                    # Название: ЖК Эльбрус, кол-во этажей: 30
# print(h1)                                                                 # Название: ЖК Акация, кол-во этажей: 30
# print(h1 == h2)                                                           # False
# h1 += 10 # __iadd__                                                       # True
# print(h1)                                                                 # False
# h2 = 10 + h2 # __radd__                                                   # True
# print(h2)                                                                 # False
# print(h1 > h2) # __gt__                               # Примечания: # Методы __iadd__ и __radd__ не обязательно описывать заново
# print(h1 >= h2) # __ge__                                            # , достаточно вернуть значение вызова __add__.
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__


class House:
    "класс для домов"

    def __init__(self, name: str, number_of_floors: int):
        if not isinstance(number_of_floors, int):
            raise TypeError('numberOfFloors должен быть целым числом')
        if not isinstance(name, str):
            raise TypeError('buildingType должен быть строкой')
        self.name = name
        self.number_of_floors = number_of_floors
        self.__str__()

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

# h1 = House('ромашка', 20)
# h2 = House('календула', 30)
# print(h1)
# h1 += 5
# print(h1)
# print(h2)
# print(h1 > h2)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)
h1 = h1 + 10
print(h1)

print(h1 == h2)
h1 += 10
print(h1)
h2 = 10 + h2
print(h2)
print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__