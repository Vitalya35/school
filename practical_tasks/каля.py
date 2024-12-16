# x = input('namber x: ')
# y = input('namber y: ')
# if x > y:
   # print('yes')
# else:
   # print('no')
import random


# x = int(input('namber: '))
# if x >= 1000 and x <= 9999 :
   #  print('ok')
# else:
    # print('not ok')

#x = int(input('storona x: '))
#y = int(input('storona y: '))
#z = int(input('storona z: '))
#if (y + z) >= x and (x + z) >= y and (x + y) >= z:
   # print('ok')
#else:
    #print('no')

# x = int(input('hour: '))
# if 5 <= x <= 11:
    # print('utro')
# elif 12 <= x <= 17:
    # print('den')
# elif 18 <= x <= 22:
    # print('veher')
# elif 23 <= x <= 24 or 0 <= x <= 4:
    # print('noch')
 # x = int(input('namber: '))
 # if 1 <= x <= 5:
     # print('bydni')
 # elif 6 <= x <= 7:
     # print("vihodnoi")

# x = int(input('namber: '))
# if x == 0:
#     print('nol')
# elif x > 0 and x % 2 == 0:
#     print('pologitelnoe chotnoe')
# elif x > 0 and x % 2 == 1:
#     print('pologitelnoe ne chotnoe')
# elif x < 0 and x % 2 == 1:
#     print('otricatelnoe ne chotnoe')
# else:
#     print('otricatelnoe chislo')


# x = {'name': 'nella', 'namee':'lera', 'nname': 'sasa'}
# y = dict(naame='vitalya',namme='mama')
# z = dict(ima='vika',imai='alisa')
# del z['ima']
# print(z)
# print(z.get('ima'))
# z['ima'] = 'vika'
# print(z)
# print(x.get('name'))
# print(x['name'])
# a = x.pop('name')
# print(x)
# print(a)

# x = {'ad':123,'sd':321}
# ad = x.pop('ad')
# print(x)
# print(ad)

                                                #  -------------------- while ------------------ #

# i = 0
# while 1:
#     if i == 3:
#         break
#     print(i)  # ----->         0  1  2
#     i += 1

# A = int(input('A: '))
# B = int(input('B: '))
# while A > B:                 # Пользователь вводит числа A и B (A > B). Выведите четные числа от A до B включительно.
#     if A % 2 == 0:
#         print(A)
#     A -= 1

# A = int(input('A: '))
# B = int(input('B: '))
# while A < B:
#     if B % 3 == 0:
#         print(B)        # Пользователь вводит числа A и B (A < B, A меньше B). Выведите числа от A до B включительно, которые делятся на три.
#     B -= 1

# x = 0
# while True:
#     n = int(input('n: '))
#     if n != 0:
#         x += n
#     else:                # Пользователь вводит числа до тех пор, пока не введет 0. Выведите сумму введенных чисел (0 считать не нужно).
#         break
# print(x)

# n = int(input('n: '))
# x = 0                      # Пользоватеxль вводит числа до тех пор, пока не введет 0. Выведите максимальное введенное число (0 считать не нужно).
# while n != 0:
#     if n > x:
#         x = n
#     elif n == 0:
#         break
#     n = int(input('n: '))
# print(f'максимальное число {x}')

# n = int(input('n: '))
# x = 0                         # Пользователь вводит числа до тех пор, пока не введет 0. Выведите минимальное введенное число (0 считать не нужно).
# while n != 0:
#     if n < x or x == 0:
#         x = n
#     elif n > x:
#         pass
#     n = int(input('n: '))
# print(f'минимальное число {x}')

# n = int(input('n: '))
# x = 1
# while n > 1:                                                   # Пользователь вводит число N. Выведите факториал число N.
#     x *= n
#     n -= 1
# print(f'факториал = {x}')

                                        # ------------------------ for ------------------------- #

# n = int(input('namber: '))
# for x in range(0,n+1):                           # Пользователь вводит число N. Выведите все числа от 0 до N включительно.
#      print(x)

# K = int(input('namber K: '))
# N = int(input('namber N: '))                     # Пользователь вводит числа K и N. Выведите все числа от K до N включительно.
# for i in range(K,N+1):
#     print(i)

# K = int(input('namber K: '))
# N = int(input('namber N: '))
# x = 0                                            # Пользователь вводит числа K и N. Выведите сумму чисел от K до N включительно.
# for i in range(K,N+1):
#     x += i
# print(x)

# K = int(input('namber K: '))
# N = int(input('namber N: '))
# x = 0                                            # Пользователь вводит числа K и N. Выведите сумму только четных чисел от K до N включительно.
# for i in range(K,N+1):
#     if i %2 == 0:
#         x += i
# print(x)

# n = int(input('введите число: '))         # Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).
# x = 0
# for i in range(n+1):
#     x += 1 + (i / 10)
# print(f'сумма десятичных чисел {round(x,1)}')

# n = int(input('введите число: '))         # Пользователь вводит число N. Найдите сумму чисел: 1 + 1/2 + 1/3 + ... + 1/N
# x = 0
# for i in range(1,n+1):
#         x += 1 / i
# print(f'сумма дробных чисел {round(x,3)}')

                                                       # функции

# a = int(input('storona a: '))
# b = int(input('storona b: '))
# def perimetor (a,b):                      # Напишите функцию perimetr, вычисляющую периметр прямоугольника со сторонами a и b
#     return (a + b) * 2
# p = perimetor(a,b)
# print(p)

# x = int(input('x: '))
# def namber(x):
#     return x % 2 == 0                    # Напишите функцию isEven, возвращающую True, если число четное, и False, если - нечетное.
# chislo = namber(x)
# print(chislo)

# r = int(input('radius: '))
# def krug(r):
#     return 3.14 * r**2                         # площадь круга
# x = krug(r)
# print(f'площадь круга = {x}')


# x = [1,2,3,4,5,6,7,8,9]
# def listt(x):
#     return x                                  # Напишите функцию, которая возвращает максимальный элемент из переданного в нее списка.
# print(max(listt(x)))


# namber = [1,2,3,4,5,6]
# def even (namber):
#     return namber                             # сумма списка
#
# x = even(namber)
# print(sum(x))

# mylist = [1, 10, 2, 4, 6]                      # Напишите функцию, которая возвращает количество четных элементов в списке.
# def chetnie(mylist):
#     x = 0
#     for i in mylist:
#         if i % 2 == 0:
#             x += 1
#     return x
# print(chetnie (mylist))


# spisok = [1, 7, 1, 5, 8, 8, 4, 7, 1, 8, 5, 6, 2, 6, 4,8]  # Напишите функцию, которая возвращает список с уникальными (неповторяющихся) элементам.
# spisok2 = [5, 8, 4, 6, 5, 8, 4, 8, 2, 4, 5, 6, 9, 5, 4, 8]
# def unikal(*a):
#     x = set(*a)
#     return f'уникальные элементы спика: {x}'
#
# print(unikal(spisok))
# print(unikal(spisok2))

                                    #    ---------------------------- F' строки ' ----------------------------     #

# from math import pi
# print(f'значение числа pi {pi:2f}')

# x = 10
# y = 20
# name = 'vity'
# print(f'{name} {x + y} лет, это значит {x} + {y} = {x + y} лет')

# planet = ['меркурий', "венера","земля","марс"]
# print(f'мы живем на планете {planet[2]}')

# planet = {'name': "Земля", 'radius': 6378000}
# print(f'Планета {planet['name']}, и ее радиус состовляет {planet['radius']/ 1000} км')

# dig = {0:'ноль', 'one': 'один'}
# print(f'0 - {dig[0]}, 1 - {dig['one']}')

# name = ('vitalya')
# print(f'имя: {name.upper()}')

# print(f'13/3 = {round(13/3)}')
# print(f'12/2 = {12//2}')


# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))
# print(a + b + c)

# a = int(input('a: '))
# b = int(input('b: '))
# print(a * b)

# a = int(input('a: '))
# b = int(input('b: '))
# print((a * 2) + (b * 2))

# r = int(input('P: '))
# pi = 3.14
# print(pi * r**2)

# a = float(input('a: '))                                   #   1.123
# b = float(input('b: '))                                   #   1.123
# c = float(input('c: '))                                   #   1.123
# print(round(a + b + c,2))                                 #   3.37

# n = int(input('n: '))                               # школьников
# k = int(input("k: "))                               # яблок
# print(k // n ,'яблок получит каждый школьник')
# print(k % n , 'яблока останется в корзине')
# print(f'{k//n} яблок получит каждый школьник \n{k%n} яблока останется в корзине')           # f' строчка в print

# a = 1594384
# n = a % 10                                                               # последняя цифра в числе
# print(n)                                                                 # 4

# a = 23
# b = a % 10
# c = a // 10
# z = b + c
# print(z)                                                                   # 2 + 3 = 5

# a = 234
# b = a % 10
# c = a // 10 % 10
# d = a // 100
# z = b + d + c
# print(z)                                                                    # 2 + 3 + 4 = 9

# a = int(input('a: '))
# b = a % 10
# c = a // 10 % 10                                                           # "Все цифры данного числа различны".
# d = a // 100
# print(b == c or b == d or c == d)

# x = [1, 2, 5, 9, 5, 6, 1, 4, 7, 3, 8, 4, 2, 6]
# z = 0
# c = []
# for i in range(len(x)):
#     print(i, x[i])


# print(f'количество четных: {z}')
# print('_'*30,'>')
# print(c)

# x = [2, 4, 6, 8, 10, 5, 7, 12, 14, 16, 18, 20]
# for i in x:                                             # Создайте список из 10 четных чисел и выведите его с помощью цикла for
#     if i % 2 == 0:
#         print(i)

# x = [1, 2, 3, 4, 5]                 # Создайте список из 5 элементов. Сделайте срез от второго индекса до четвертого
# print(x[1:4])


# from random import randint
# x = []                            # Создайте пустой список и добавьте в него 10 случайных чисел и выведите их.
# for i in range(10):
#     x.append(randint(1,10))
#
# print(f'список: {x}')
#
# x.clear()        # Удалите все элементы из списка, созданного в задании 3
# print(x)




# def list_():
#     z = input('Введите имя: ')
#     a = z.replace('a', '')  # Создайте список из введенной пользователем строки и удалите из него символы 'a', 'e', 'o'
#     x = a.replace('e', '')
#     z = x.replace('o', '')
#     print(z)


# def dva_spiska(a, b):
#     c = []
#     for i in a:
#         if i not in b:      # Даны два списка, удалите все элементы первого списка из второго
#             c.append(i)
#
#     print(c)
#
# if __name__ == '__main__':
#     dva_spiska([1,89,3,3,4,5,8,9,6,5,4], [2,4,5,9,8,7,4,5,6,4,8,3,1,5])
#

# z = [1,5,9,7,6,4,8,3,2,5]  # Создайте список из случайных чисел и найдите наибольший элемент в нем.
# print(max(z))
# print(min(z))              # Найдите наименьший элемент в списке
# print(sum(z))              # Найдите сумму элементов списка
#
# def srednee_arifmeticheskoe():                             # Найдите среднее арифметическое элементов списка
#     print(f'среднее арефметическое списка z: {sum(z)//len(z)} ')
#
# srednee_arifmeticheskoe()


# z = [5, 6, 4, 3, 2]                  # Найдите номер его последнего локального максимума
# x = max(z)
# max_indeks = z.index(x)
# print(max_indeks)


                               # Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в
                               # формате: название фрукта и его количество. Добавьте все фрукты в словарь, где
                               # название фрукта - это ключ, а количество - значение.

# chislo_fruktov = (int(input('chislj fruktov: ')))
# frukt = (input('frukt: '))
# z = {}
# z.setdefault(chislo_fruktov, frukt)
# print(z)


# z = {}
# chislo_fruktov = (int(input('количество фруктов: ')))
# for i in range(chislo_fruktov):
#     frukt = input('фрукт: ')
#     kolvo_fruktov = input('кол-во фруктов: ')
#     z[frukt] = kolvo_fruktov
#
# print(z)


                                    # 1. Пользователь вводит число N.
                                    # 2. Затем он вводит личные данные (имя и возраст) своих N друзей.
                                    # 3.  Создайте список friends
                                    # 4. И добавьте в него N словарей с ключами name и age.
                                    # 5. Найдите самого младшего из друзей и выведите его имя.
# N = int(input('число товарищей: '))
# friends = []
# min_i = 0
# min_age = 100
# for i in range(N):
#     name = input('имя: ')
#     age = int(input('возраст: '))
#     if age < min_age:
#         min_age = age
#         min_i = i
#     friends.append({'name': name, "age": age})
#
# print(friends)
# print(friends[min_i]['name'])


                             # 1 Пользователь вводит число N.
                             # 2 Затем он вводит личные данные (имя и возраст) своих N друзей.
                             # 3 Создайте список friends и добавьте в него N словарей с ключами name и age.
                             # 4 Выведите средний возраст всех друзей и самое длинное имя.

# N = int(input('число товарищей: '))
# friends = []
# dlinnoe_imya = ''
# max_i = 0
# x = []
# sredn_age = 0
# for i in range(N):
#     name = input('name: ')
#     age = int(input('age: '))
#     x.append(age)
#     sredn_age = sum(x) // len(x)
#     if len(name) > len(dlinnoe_imya):
#         dlinnoe_imya = name
#         max_i = i
#     friends.append({'name': name, 'age': age})
#
#
# print(friends[max_i]['name'])
# print(sredn_age)


# print(1.01 ** 365)
# print(0.99 ** 365)

                                                 #        ------------------- ФАЙЛЫ ------------------       #
import  io
from pprint import pprint

# x = 'asd.txt'
# file = open(x, 'r')                               #  «read»
# pprint(file.read())                               # чтение файла
# file.close()

# file = open('asd.txt', 'r')
# pprint(open('asd.txt', 'r').read())               # чтение файла
# file.close()

# z = 'zxc.txt'
# file = open(z, 'w')                               # запись в файл(создание)
# file_1.write('привет')
# file_1.close()

# file_1 = open('zxc.txt', 'w')                       #  «write»
# file_1.write('привет    ')                              # запись в файл(создание)
# file_1.close()
#
# file_1 = open('zxc.txt', 'r')
# pprint(file_1.read())
# # file_1.close()
#
# file_1 = open('zxc.txt', 'a')                       # «append»
# file_1.write('\nздрасти')                              # добовление в файл(создание)
# file_1.close()

# file_1 = open('zxc.txt', 'r')
# pprint(file_1.read())
# # file_1.close()

# # x = 'zxc.txt'
# file_1 = open('x ', 'a')                       # «append»
# file_1.write('\nмордасти')                              # добовление в файл(создание)
# file_1.close()
#
# file_1 = open('zxc.txt', 'r')
# pprint(file_1.read())
# file_1.close()

# with open('asd.txt', 'a') as x:
#     x.write('poka\n')
#                                  -----------------------------------------------------------------------------

import os


def slozhit(a, b):


    if float(int(b)):
        c = a + str(b)
    elif

        return c


print(slozhit(3.3,  'asd' ))

# str_a = '50.85'
# b = 10.33
# c = float(str_a) + b
# print ("The value of c = ",c)

str_a = '5,123,000'
int_b = int(str_a.replace(',',''))
print ("The integer value",int_b)

