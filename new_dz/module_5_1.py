# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
#  Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
# Пункты задачи:
# Создайте класс House.
# Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
# Внутри метода __init__ создайте атрибуты объекта self.name и self.number_of_floors,
# присвойте им переданные значения.
# Создайте метод go_to с параметром new_floor и напишите логику внутри него на основе описания задачи.
# Создайте объект класса House с произвольным названием и количеством этажей.
# Вызовите метод go_to у этого объекта с произвольным числом.
# Исходные данные:                      # Вывод на консоль:
# h1 = House('ЖК Горский', 18)                              # 1
# h2 = House('Домик в деревне', 2)                          # 2
# h1.go_to(5)                                               # 3
# h2.go_to(10)                                              # 4
                                                            # 5
                                                            # "Такого этажа не существует"


class House:
    "класс для домов"
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        self.new_floor = new_floor
        if self.new_floor > self.number_of_floors or self.new_floor < 1:
            print(f"Такого этажа в {self.name} не существует")
        else:
            for i in range(1, self.new_floor + 1):
                print(f'{self.name}, едем, этаж {i}')



H1 = House('жига_сити', 12)
H1.go_to(13)
H2 = House('кибер дом', 15)
H2.go_to(5)
H2.go_to(16)

# print(House.__doc__)
# print(House.__dict__)