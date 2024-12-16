# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
    # Создать переменную calls = 0 вне функций.
    # Создать функцию count_calls и изменять в ней значение переменной calls.
    # Эта функция должна вызываться в остальных двух функциях.
     # Создать функцию string_info с параметром string и реализовать логику работы по описанию.
      # Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
    # Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
    # Вывести значение переменной calls на экран(в консоль).
# Пример выполняемого кода:
# print(string_info('Capybara'))
# print(string_info('Armageddon'))
# print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
# print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
# print(calls)
                                       # (8, 'CAPYBARA', 'capybara')
                                       # (10, 'ARMAGEDDON', 'armageddon')
# Вывод на консоль:                    # True
                                       # False
                                       # 4
# Для использования глобальной переменной внутри функции используйте оператор global.
# Для функции is_contains лучше привести и искомую строку и все строки в списке в один регистр.

calls = 0
def count_calls():
    global calls
    calls += 1
    return calls

def string_info(string=str):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string=str, list_to_search=list):
    count_calls()
    n_list_to_search = []
    for i in list_to_search:
        n_list_to_search.append(i.upper())
    if string.upper() in n_list_to_search:
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle',['recycling', 'cyclic']))
print(calls)