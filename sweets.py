# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?

from random import randint


# правка неправильного ввода
def correct_input(temp, x1):
    k = max_one_time
    if temp < max_one_time:
        k = temp
    while not (0 < x1 < k + 1):
        x1 = int(input("Требуется корректный ввод : "))
    return x1


# выбор игрока (бот или человек)
def who_is_players():
    print("Вы будете играть с ботом или с другом ? ")
    while 1:
        x = input("Если с ботом , то нажмите  \"B\",если с другом , то \"F\"")
        if x.lower() == "b" or x.lower() == "f":
            return x
        else:
            print("Требуется корректный ввод ")
    return x.lower()


def moves(temp):
    k = max_one_time
    b1 = input("Хотите подсказку ? Нажмите  'Y' если Да ")
    if b1 == "y":                                             # мои ходы
        x1 = temp % (max_one_time + 1)
        if not x1:
            print("Выйгрыш невозможен, если противниk правильно будет ходить ")
            x1 = int(input("Сколько вы хотите взять конфет ? "))
        print(f"Вы взяли {x1} конфет ")
    else:
        x1 = int(input("Сколько вы хотите взять конфет ? "))
        x1 = correct_input(temp, x1)
    temp -= x1
    if not temp:
        return -1                                            # если мой выйгрыш
    print(f"Осталось {temp} конфет ")
    print("-----------------------")
    if who == "b":                                           # просчет ходов для бота
        x1 = temp % (max_one_time + 1)
        if not x1:
            if temp <= max_one_time:
                k = temp
            x1 = randint(1, k)                               # выбор ходов для бота,если нет возможности выйграть
        temp -= x1
        if not temp:
            return -2                                         # если  выйгрыш бота
        print(f"Бот взял {x1} конфет ")
    elif who == "f":                                         # ходы соперника
        x1 = int(input("Сколько ваш друг хочет взять конфет ? "))
        x1 = correct_input(temp, x1)
        temp -= x1
        if not temp:
            return -3                                        # если выйгрыш соперника
    print(f"Осталось {temp} конфет ")
    return temp


max_one_time = int(
    input("Введите количество конфет которое можно взять за один раз: "))
number_candies = int(input("Введите количество конфет : "))


rest = number_candies                                       # остаток
who = who_is_players()

while rest > 0:
    steps = moves(rest)
    rest = steps

str_ = ["ваш друг", "бот", "я"]
print(f"В этой игре выйграл {str_[rest]}")
print("--------------------------")
