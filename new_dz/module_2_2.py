# На вход программе подаются 3 целых числа и записываются в переменные first, second и third
# соответственно.Ваша задача написать условную конструкцию (из if, elif, else),
# которая выводит кол-во одинаковых чисел среди 3-х введённых.
#
# Пункты задачи:
# Если все числа равны между собой, то вывести 3
# Если хотя бы 2 из 3 введённых чисел равны между собой, то вывести 2
# Если равных чисел среди 3-х вообще нет, то вывести 0

first = int(input('first: '))
second = int(input('second: '))
third = int(input('third: '))
if first == second == third:
    print(3)
elif first != second and first != third and second != third:
    print(0)
elif first == second or first == third or second == third:
    print(2)
