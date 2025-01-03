# Создайте функцию custom_write(file_name, strings), которая принимает аргументы file_name - название файла для записи,
# strings - список строк для записи.
# Функция должна:
# Записывать в файл file_name все строки из списка strings, каждая на новой строке.
# Возвращать словарь strings_positions, где ключом будет кортеж (<номер строки>, <байт начала строки>),
# а значением - записываемая строка. Для получения номера байта начала строки используйте метод tell() перед записью.
# Пример полученного словаря:
# {(1, 0): 'Text for tell.', (2, 16): 'Используйте кодировку utf-8.'}
# Где:
# 1, 2 - номера записанных строк.
# 0, 16 - номера байт, на которых началась запись строк.
# 'Text for tell.', 'Используйте кодировку utf-8.' - сами строки.
#
# Пример результата выполнения программы:
# Пример выполняемого кода:
# info = [
#     'Text for tell.',
#     'Используйте кодировку utf-8.',
#     'Because there are 2 languages!',
#     'Спасибо!'
#     ]
#
# result = custom_write('test.txt', info)
# for elem in result.items():
#   print(elem)
#
# Вывод на консоль:
# ((1, 0), 'Text for tell.')
# ((2, 16), 'Используйте кодировку utf-8.')
# ((3, 66), 'Because there are 2 languages!')
# ((4, 98), 'Спасибо!')

import io


info = ['Text for tell.', 'Используйте кодировку utf-8.', 'Because there are 2 languages!', 'Спасибо!']

def custom_write(file_name, strings):
    count = 0
    strings_positions = {}
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in strings:
            x = file.tell()
            file.write(str(f'{i}\n'))
            count += 1
            strings_positions[(count, x)] = i
    return strings_positions.items()

x = custom_write('filllllle.txt', info)

for i in x:
    print(i)
