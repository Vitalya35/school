# Напишите 2 функции:
# Функция, которая складывает 3 числа (sum_three)
# Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
# "Составное" в противном случае.
# Примечания:
# Не забудьте написать внутреннюю функцию wrapper в is_prime
# Функция is_prime должна возвращать wrapper
# @is_prime - декоратор для функции sum_three


def is_prime(func):
    def wrapper(*args, **kwargs):
        if func(*args, **kwargs) == 0:
            return f'рациональное \n {func(*args, **kwargs)}'
        elif func(*args, **kwargs) == 1:
            return f'число является автоморфным числом в любой позиционной системе счисления \n {func(*args, **kwargs)}'
        elif func(*args, **kwargs) == 2:
            return f'Простое \n {func(*args, **kwargs)}'
        elif func(*args, **kwargs) > 1:
            flag = False
            while flag == False:
                for i in range(2, func(*args, **kwargs)):
                    if func(*args, **kwargs) % i == 0:
                        flag = True
                        break
                if flag == False:
                    return f'Простое \n {func(*args, **kwargs)}'
                elif flag == True:
                    return f'Составное \n {func(*args, **kwargs)}'
    return wrapper

@is_prime
def sum_three(x, y, z):
    result = x + y + z
    return result

print(x := sum_three(0, 0, 9))

# Пример:
# result = sum_three(2, 3, 6)
# print(result)
# Результат консоли:
# Простое
# 11
