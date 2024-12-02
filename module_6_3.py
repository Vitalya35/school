# Animal - класс описывающий животных.
# Класс обладает следующими атрибутами:
# live = True
# sound = None - звук (изначально отсутствует)
# _DEGREE_OF_DANGER = 0 - степень опасности существа
# Объект этого класса обладает следующими атрибутами:
# _cords = [0, 0, 0] - координаты в пространстве.
# speed = ... - скорость передвижения существа (определяется при создании объекта)
# И методами:
# move(self, dx, dy, dz), который должен менять соответствующие координаты в _cords на dx, dy и dz в том же порядке,
# где множителем будет являться speed. Если при попытке изменения координаты z в _cords значение будет меньше 0,
# то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносятся.
# get_cords(self), который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
# attack(self), который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" ,
# если равно или больше.
# Bird - класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
# beak = True - наличие клюва
# И методом:
# lay_eggs(self), который выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"
# AquaticAnimal - класс описывающий плавающего животного. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 3.
# Должен обладать методом:
#       dive_in(self, dz) - где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z в _coords.
# Чтобы сделать dz положительным, берите его значение по модулю (функция abs).
# Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
# PoisonousAnimal - класс описывающий ядовитых животных. Наследуется от Animal.
# В этом классе атрибут _DEGREE_OF_DANGER = 8.
# Duckbill - класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
# Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
# sound = "Click-click-click" - звук, который издаёт утконос
# По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.
# После чего утконос совершает манёвры и ныряет.
# Теперь утконос в безопасности, он откладывает яйца для будущего потомства.
# Примечания:
# Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании:
# при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"
import random


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]

    def __init__(self, speed):
        self.speed = speed

    def move(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        if self.z < 0:
            return print("It's too deep, i can't dive :(")
        else:
            self._cords[0] = self.x * self.speed
            self._cords[1] = self.y * self.speed
            self._cords[2] = self.z * self.speed
        return self._cords

    def get_cords(self):
        return print(f'X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        elif self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        return print(f"Here are(is) {random.randint(1, 4)} eggs for you")

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self.dz = dz
        super()._cords[2] = (abs(self.z - self.dz) * self.speed // 2)
        super()._cords[0] = self.x * (self.speed // 2)
        super()._cords[1] = self.y * (self.speed // 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(Bird, PoisonousAnimal, AquaticAnimal):
    sound = "Click-click-click"

    def speak(self):
        return print(f'{self.sound}')




db = Duckbill(10)                             # Вывод на консоль:
print(db.live)                                # True
print(db.beak)                                # True
db.speak()                                    # Click-click-click
db.attack()                                   # Be careful, i'm attacking you 0_0
db.move(1, 2, 3)                     # X: 10 Y: 20 Z: 30
db.get_cords()                                # X: 10 Y: 20 Z: 0
db.dive_in(6)                                 # Here are(is) 3 eggs for you # Число может быть другим (1-4)
db.get_cords()
db.lay_eggs()