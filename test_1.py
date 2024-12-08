import random

FAMOUS_PEOPLE = {"Александр Сергееви Пушкин" : "26.06.1799", "Михаил Юрьевич Лермонтов" : "15.10.1814","Сергей Александрович Есенин" : "03.10.1893", "Владимир Семенович Высоцкий" : "25.01.1938", "Виктор Робертович Цой" : "21.06.1962",
                    "Константин Эдуардович Шиопсковский" : "17.09.1837", "Сергей Павлович Королёв" : "12.01.1907", "Валентин Петрови Глушко" : "20.08.1908", "Андрей Николаевич Тупопев" : "29.10.1888", "Юрий Алексеевич Гагарин" : "09.03.1934"}

def start():
    rounds = int(input('Сколько раз вы хотите играть?'))
    for i in range (rounds):
        name,date = random.choice(list(FAMOUS_PEOPLE.items()))
        answer = input(f'Когда родился {name}')

        if answer == date:
            print('Верно')
        else:
            print('Неверно')

    print('Пока')