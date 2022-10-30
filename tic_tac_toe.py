
#  крестики нолики

'''
                  -------------
                  | 1 | 2 | 3 |       ввод осуществлять 
                  -------------
                  | 4 | 5 | 6 |       цифрами по этой схеме
                  -------------
                  | 7 | 8 | 9 |       от 1 до 9
                  -------------


'''
# обработка 
def processing(t, t1):
    for i in range(8):
        for j in range(3):
            if t == win_option[i][j]:
                win_option[i][j] = t1
            if sum(win_option[i]) == 300 or sum(win_option[i]) == 600:
                return sum(win_option[i])
    return 0


# передача хода
def change_move(k):
    if k == 200:
        k = 100
    else:
        k = 200
    return k


# вывод таблицы
def print_table():
    slice_ = win_option[:3]

    for i in slice_:
        str_ = list(map(func, i))
        print(*str_, sep="  ")

        
# обработка для вывода на экран пользовательских значений
def func(i):
    if i == 200:
        return "x"
    if i == 100:
        return "0"
    return "-"


# обработка ввода
def correct_input(move):
    slice_ = win_option[slice(0,3)]
    print("сейчас ваш ход " if move == 200 else "сейчас ход вашего соперника")
    while True:
        s = int(input('введите номер ячейки от 1 до 9    '))
        s1=any([s in i for i in slice_])
        if s > 9 or s < 1:
            s = int(input('введите корректные цифры    '))
        elif not s1:
            print(" такая ячейка уже была , повторим ввод ")
        else:
            return s
        

# список выйгрышных вариантов
win_option = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
     [1, 4, 7], [2, 5, 8], [3, 6, 9],
     [1, 5, 9], [3, 5, 7]]


d = 0     # при d = 300    sum[100,100,100] выйграл соперник
          # при d = 600    sum[200,200,200] я выйграл

k = 0     # переход хода : 100 - соперник
          # переход хода : 200 - я

while d < 300:
   
    
    k = change_move(k)
    s = correct_input(k)                   
    d = processing(s, k)
    print_table()
    
    if d:
        print("вы победитель " if d == 600 
        else "ваш соперник выйграл")
    
