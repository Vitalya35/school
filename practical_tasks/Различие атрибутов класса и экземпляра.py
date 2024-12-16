# Создайте новый класс Buiding с атрибутом total.
# Создайте инициализатор для класса Buiding,
# который будет увеличивать атрибут количества созданных объектов класса Building total.
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print.
# Полученный код напишите в ответ к домашнему заданию.
from random import randint
import random
from random import choice, sample
import string


class Building:
    Total = 0

    def __init__(self):
        Building.Total += 1

    def __str__(self):
        return f'Building number {Building.Total}'


for i in range(40):
    new_building = Building()
    print(new_building)




# def vital(r, d):
#     def generate_string():
#         result = ''.join(random.choice(string.ascii_lowercase) for _ in range(d))
#         return result
#
#     e = 0
#     while e < r:
#         print(generate_string())
#         e += 1


