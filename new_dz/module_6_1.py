# Создайте: 2 класса родителя: Animal, Plant
# Для класса Animal атрибуты alive = True(живой) и fed = False(накормленный), name - индивидуальное название каждого животного.
# Для класса Plant атрибут edible = False(съедобность), name - индивидуальное название каждого растения
# 4 класса наследника:
# Mammal, Predator для Animal.
# Flower, Fruit для Plant.
#   У каждого из объектов класса Mammal и Predator должны быть атрибуты и методы:
# eat(self, food) - метод, где food - это параметр, принимающий объекты классов растений.
# В данном случае можно использовать принцип наследования, чтобы не дублировать код.
# Метод eat должен работать следующим образом:
# Если переданное растение (food) съедобное - выводит на экран "<self.name> съел <food.name>", меняется атрибут fed на True.
# Если переданное растение (food) не съедобное - выводит на экран "<self.name> не стал есть <food.name>", меняется атрибут alive на False.
# Т.е если животному дать съедобное растение, то животное насытится, если не съедобное - погибнет.
# У каждого объекта Fruit должен быть атрибут edible = True (переопределить при наследовании)
#   Пункты задачи:
# Создайте классы Animal и Plant с соответствующими атрибутами и методами
# Создайте(+унаследуйте) классы Mammal, Predator, Flower, Fruit с соответствующими атрибутами и методами.
# При необходимости переопределите значения атрибутов.
# Примечания:
# Помните, обращаясь к атрибутам объекта текущего класса используйте параметр self.
# Передавая объекты классов Fruit и Flower в метод eat, так же можно обращаться к их атрибутам внутри.
# Обращайте внимание на то, где атрибут класса, а где атрибут объекта.

class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        self.food = food
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False

class Mammal(Animal):
    pass

class Predator(Animal):
    pass


class Plant:
    edible = False

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
print(a1.name)                                                    # Волк с Уолл-Стрит
print(p1.name)                                                    # Цветик семицветик
print(a1.alive)                                                   # True
print(a2.fed)                                                     # False
a1.eat(p1)                                                        # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)                                                        # Хатико съел Заводной апельсин
print(a1.alive)                                                   # False
print(a2.fed)                                                     # True
