import time
import random
import sys
import os
import re

os.system('cls')

def game_pole(data):
    ''' Отрисовка игрового поля
    Args: [] - список текстовых и строковых значений отражающих текущую игровую ситуацию 
    input: () 
    Reterns: print - отрисовка игрового поля с текущей игровой ситуацией

    '''
    print("-" * 13)
    print("|", data[0], "|", data[1], "|", data[2], "|")
    print("-" * 13)
    print("|", data[3], "|", data[4], "|", data[5], "|")
    print("-" * 13)
    print("|", data[6], "|", data[7], "|", data[8], "|")
    print("-" * 13)

def input_name():
    ''' Ввод имен игроков и жеребьевка
    
    Args: ()  
    input: name1 (str) имя первого игрока, name2 (str) имя второго игрока
    Reterns: print: результат жеребьвки, name1 (str) имя первого игрока, name2 (str) имя второго игрока, и результат жеребьевки int 1 или int 2 '''

    name1 = input('Первый игрок, представьтесь пожалуйста:\n')
    name2 = input('Второй игрок, представьтесь пожалуйста:\n')
    print('Подождите идет жеребьевка')
    time.sleep(1)
    t = random.randint(1, 2)
    if t == 1:
        print(f'Игрок {name1} играет за X Игрок {name2} играет за 0')
        return(name1, name2, 1)
    else:
        print(f'Игрок {name1} играет за 0 Игрок {name2} играет за X')
        return(name1, name2, 2)

def game_play(name1, name2, token, data, count):
    ''' Игровой ход. Отображается игровое поле с текущей игровой ситуацией. Игрок выбирает куда поставить крестик или нолик.
        Проводится проверка на корректность ввода. Результат ввдда проверяется на выигрыш.
        В случае отсутствия выигрыша ход повторяется

        Args: name1 (str) - имя одного игрока, name2 - имя другого игрока (str), token (str) - X или 0, data [] - список
        текстовых и строковых значений отражающих текущую игровую ситуацию, count (int) - счетчик

        Input: temp (int) числа от 1 до 9 - выбор поля для X или 0, функция game_pole(data) - отрисовка игровой ситуации, 
        функция checking_win(data, count, name) - для проверки вариантов окончания игры.
        
        Reterns: game_play(name1, name2, token, data, count) - рекурсия функции для следующего хода '''

    game_pole(data)
    name = name1
    temp = input(f'Игрок {name}, выберите номер поля на который ставим {token}:  ')
    if not re.match(r'^[1-9]$', temp):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return game_play(name1, name2, token, data, count)
    elif data[int(temp)-1] == '0':
        print ('Поле занято. Попробуйте еще раз')
        return game_play(name1, name2, token, data, count)
    elif data[int(temp)-1] == 'X':
        print ('Поле занято. Попробуйте еще раз')
        return game_play(name1, name2, token, data, count)
    else:
        temp = int(temp)
        data[temp-1] = token
        checking_win(data, count, name)
        count += 1
        name1 = name2
        name2 = name
        if token == 'X':
            token = '0'
            return game_play(name1, name2, token, data, count)
        else:    
            token = 'X'
            return game_play(name1, name2, token, data, count)  

def name_win(data, name):
    ''' Отрисовка победной комбинации и поздравление победителю
        
        Args: name (str) - имя игрока сделавшего последний ход, data [] - список
        текстовых и строковых значений отражающих текущую игровую ситуацию

        Input: функция game_pole(data) - передача параметров для отрисовки игровой ситуации, 
                
        Reterns: функция game_pole(data) - отрисовка итоговой игровой ситуации, print - поздравления победителю,
        перезапуск игры в зависимости от переменной num  '''
                
    game_pole(data)
    print(f'Поздравляю! {name}, ты победитель!!!')
    num = input('Если хотите сыграть еще раз введите 1, если хотите закончить игру, нажмите ввод   ')
    if num == '1':
        start_game()
    else:
        sys.exit()

def checking_win(data, count, name):
    ''' Проверка на выигрышные комбинации и состояние ничьей. В случае ничьей, отрисовка итоговой
        игровой комбинации и сообщение об окончании игры.
    
        Args: name (str) - имя игрока сделавшего последний ход, data [] - список текстовых и строковых
        значений отражающих текущую игровую ситуацию, count (int) - счетчик

        Input: Вызов функции name_win(data, name) и прердача в нее аргументов data [] и name (str),
        вызов функции game_pole(data) и прердача в нее аргумента data []
        
        Reterns: передача исполнения программы  в функцию name_win(data, name), функция game_pole(data)
        - отрисовка итоговой игровой ситуации, print - сообщение о ничьей,
        перезапуск игры в зависимости от переменной num  '''

    if data[0] == 'X' and data[1] == 'X' and data[2] == 'X':
        name_win(data, name)
    elif data[3] == 'X' and data[4] == 'X' and data[5] == 'X':
        name_win(data, name)
    elif data[6] == 'X' and data[7] == 'X' and data[8] == 'X':
        name_win(data, name)
    elif data[0] == 'X' and data[3] == 'X' and data[6] == 'X':
        name_win(data, name)
    elif data[1] == 'X' and data[4] == 'X' and data[7] == 'X':
        name_win(data, name)
    elif data[2] == 'X' and data[5] == 'X' and data[8] == 'X':
        name_win(data, name)
    elif data[0] == 'X' and data[4] == 'X' and data[8] == 'X':
        name_win(data, name)
    elif data[2] == 'X' and data[4] == 'X' and data[6] == 'X':
        name_win(data, name)
    elif data[0] == '0' and data[1] == '0' and data[2] == '0':
        name_win(data, name)
    elif data[3] == '0' and data[4] == '0' and data[5] == '0':
        name_win(data, name)
    elif data[6] == '0' and data[7] == '0' and data[8] == '0':
        name_win(data, name)
    elif data[0] == '0' and data[3] == '0' and data[6] == '0':
        name_win(data, name)
    elif data[1] == '0' and data[4] == '0' and data[7] == '0':
        name_win(data, name)
    elif data[2] == '0' and data[5] == '0' and data[8] == '0':
        name_win(data, name)
    elif data[0] == '0' and data[4] == '0' and data[8] == '0':
        name_win(data, name)
    elif data[2] == '0' and data[4] == '0' and data[6] == '0':
        name_win(data, name)
    elif count == 9:
        game_pole(data)
        print(f'Ничья!!!')
        num = input('Если хотите сыграть еще раз введите 1, если хотите закончить игру, нажмите ввод   ')
        if num == '1':
            start_game()
        else:
            sys.exit()

def start_game():
    ''' Старт игры. Создание списка для начальной игровой ситуации. Получение данных
        о именах игроков и результатах жеребьевки. Передача исполнения программы в 
        функцию game_play(name1, name2, token, data, 1)

        Args: ()

        Input: Запуск функции input_name() - и получение из нее аргументов name1 (str) - имя одного игрока,
        name2 (str) - имя другого игрока, num (int) - число 1 или 2 как результат жеребьевки. Запуск функции
        game_play и передача в нее аргументов name1 (str) - имя одного игрока, name2 (str) - имя другого
        игрока, token (str) - X так как крестики всегда начинают, data [] - список числовых значений от 1 до
        9 отражающих начальную игровую ситуацию, count (int) - число 1
        
        Reterns: Передача исполнения программы в функцию game_play (name1, name2, token, data, 1) '''
    
    name1, name2, num = input_name()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    token = 'X'
    if num == 1:
        game_play(name1, name2, token, data, 1)
    else:
        name = name1
        name1 = name2
        name2 = name
        game_play(name1, name2, token, data, 1)

print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10) # Единственная списанная строка с кононического варинта игры на Python
start_game()
