# Пример выполняемого кода (тесты):
# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
# Вывод на консоль:
# Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
# НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
# Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
# Нельзя отправить письмо самому себе!
# Примечания:

def send_email(message, recipient, *, sender="university.help@gmail.com"):
    if recipient.endswith('.com') and '@' in recipient or recipient.endswith('.ru') and '@' in recipient or recipient.endswith('.net') and '@' in recipient:
        if sender.endswith('.com') and '@' in sender or sender.endswith('.ru') and '@' in sender or sender.endswith('.net') and '@' in sender:
            if sender == "university.help@gmail.com":
                print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}')
            elif recipient == sender:
                print('Нельзя отправить письмо самому себе!')
            elif sender != "university.help@gmail.com":
                print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')
        else:
            print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    else:
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')

# send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
# send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
# send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
# send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')