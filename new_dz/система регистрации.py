class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:

    "Клавсс пользователя содержащий атрибуты: логин, пароль"

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ =='__main__':
    database = Database()
    count_isupper = 0
    count_isdigit = 0
    c = False
    while True:
        choise = int(input('Приветствую, выберите действие: \n1 - Вход\n2 - Регистрация\nВведите действие: '))
        if choise == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Вход выполнен {login}')
                    break
                else:
                    print('Неверный пароль')
            else:
                print('Пользователь не найден')
        if choise == 2:
            user = User(input('Введите логин: '), password := input('Введите пароль  состоящий из не менее 6 символов,'
                ' содержащий заглавные буквы и цифры. \nВведите пароль: '), password2 := input('Повтарите пороль:  '))
            for i in password:
                if i.isupper():
                    count_isupper += 1  # проверка на наличие букв в верхнем регистре
                if i.isdigit():
                    count_isdigit += 1  # проверка на наличие цифр
            if len(password) == 6 and count_isupper > 0 and count_isdigit > 0:
                c = True
            if c == True:
                pass
            else:
                print('Пароль не соответствует требованиям.')
                continue
            if password != password2:
                print('Пароли не совподают, попробуйте еще раз')
                continue
            database.add_user(user.username, user.password)

