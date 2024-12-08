from test_1 import *

text_1 = str(input('Привет. Ты попал на викторину. Как Тебя зовут?'))

if text_1 != '':

    text_2 = str(input('Меня Валера. Приятно познокомиться! Готов сыграть в викторину?'))

    if text_2.lower() == 'да':
        print('DEBUG')
        start()
    elif text_2.lower == 'нет':
        print('Хорошо. Удачи')
else:
    text_1 = str(input('Введи конкретное имя!'))
    if text_1 != '':
        text_2 = str(input('Меня Валера. Приятно познокомиться! Готов сыграть в викторину?'))

        if text_2.lower() == 'да':
            start()
        elif text_2.lower == 'нет':
            print('Хорошо. Удачи')

