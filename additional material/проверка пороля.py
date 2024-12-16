f = input('Введите пароль  состоящий из не менее 6 символов, содержащий заглавные буквы и цифры. \nпароль: ')

def proverka(password):
    count_isupper = 0
    count_isdigit = 0
    c = False
    for i in password:
        if i.isupper():
            count_isupper += 1      # проверка на наличие букв в верхнем регистре
        if i.isdigit():
            count_isdigit += 1      # проверка на наличие цифр
    if len(password) == 6 and count_isupper > 0 and count_isdigit > 0:
        c = True
    if c == True:
        print('Отличный пароль')
    else:
        print('Пароль не соответствует требованиям.')

proverka(f)
