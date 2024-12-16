# Необходимо дополнить класс House следующими специальными методами:
# __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
# Пример результата выполнения программы:
# Пример выполняемого кода:
# h1 = House('ЖК Эльбрус', 10)
# h2 = House('ЖК Акация', 20)
# # __str__
# print(h1)
# print(h2)
# # __len__
# print(len(h1))
# print(len(h2))
# Вывод на консоль:
# Название: ЖК Эльбрус, кол-во этажей: 10
# Название: ЖК Акация, кол-во этажей: 20
# 10
# 20


class House:
    "класс для домов"
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.__str__()

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


H2 = House('цветочек', 15)
print(H2)
print(len(H2))
