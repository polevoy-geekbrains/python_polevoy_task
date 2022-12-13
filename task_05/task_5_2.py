import time
import random
import sys
import os
import re

os.system('cls')



def type_of_game(name1):
    ''' Выбор типа игры и имени второго игрока
    
    Args: name1 (str) имя первого игрока  
    input: type_game (str) тип игры, name2 (str) имя второго игрока
    Reterns: name2 (str) имя второго игрока, type_game (str) тип игры, с ботом или с человеком '''

    
    type_game = input(f'{name1} сделайте выбор с кем Вы хотите играть:\nЕсли с другим игроком нажмите - 1\nЕсли с ботом нажмите - 2\nЕсли с умным ботом нажмите - 3\n')
    if not re.match(r'^[1-3]$', type_game):
        print (f'{name1} Вы какой-то странный, не можете выбрать одну из трех цифр. Попробуйте еще раз ')
        return type_of_game(name1)
    if type_game == '1':
        name2 = input('Второй игрок, представьтесь пожалуйста:\n')
    if type_game == '2':
        name2 = 'Бот'
    if type_game == '3':
        name2 = 'Умный Бот'
    return name2, type_game
    
    
    
def game_toss(name1, name2):
    ''' Жеребьевка, выбор name1 или name2 будет ходить первым '''

    print('Подождите идет жеребьевка')
    time.sleep(1)
    t = random.randint(1, 2)
    if t == 1:
        print(f'Первым ходит игрок {name1} ')
        return name1, name2
    else:
        print(f'Первым ходит игрок {name2} ')
        name = name1
        name1 = name2
        name2 = name
        return name1, name2

def start_game():
    ''' Начало игры. Вызов функции типа игры, с ботом или с человеком, вызов функции жеребьевки, присвоение имени первому игроку
    выбор, размера кучи, выбор сколько можно брать из кучи. Передача данных в функцию игры.'''

    name1 = input('Первый игрок, представьтесь пожалуйста:\n')
    name2, num = type_of_game(name1)
    lot_candy = input('Введите количество конфет в куче     ')
    if (not lot_candy.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return start_game()
    lot_candy = int(lot_candy)
    if lot_candy < 10:
        print('Забыл предупредить, меньше 10 конфет это уже не куча, у Вас теперь куча из 2021 конфеты')
        lot_candy = 2021
    taken_candies = input('Из кучи нельзя брать за раз больше трети первоначального количества. Сколько берем?     ')
    if (not taken_candies.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return start_game()
    elif taken_candies == '0':
        print('Похоже Вы слишком хитрый, тогда будете брать из кучи по одной конфете')
        lot_candy = 1
    elif int(taken_candies) > lot_candy // 3:
        print (f'{name1} не знает, что такое треть. Приглашаю в игру нового игрока')
        return start_game()
    else:
        taken_candies = int(taken_candies)
    
    name1, name2 = game_toss(name1, name2)
    if num == '1':
        game_play_human(name1, name2, lot_candy, taken_candies)
    elif num == '2':
        game_play_bot(name1, name2, lot_candy, taken_candies)
    else:
        game_play_smart_bot(name1, name2, lot_candy, taken_candies, 0, taken_candies)

def game_play_human(name1, name2, lot_candy, taken_candies):
    ''' Игра с другим игроком '''

    name = name1
    temp = input(f'{name} в куче {lot_candy} конфет. Сколько из них Вы возьмете?  ')
    if (not temp.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return game_play_human(name1, name2, lot_candy, taken_candies)
    temp = int(temp)
    if temp == 0:
        print ('Вы должны взять хотя бы одну конфету. Попробуйте еще раз')
        return game_play_human(name1, name2, lot_candy, taken_candies)
    elif temp > taken_candies:
        print (f'Вы не можете брать больше конфет чем: {taken_candies}. Попробуйте еще раз')
        return game_play_human(name1, name2, lot_candy, taken_candies)
    elif temp > lot_candy:
        print (f'Вы не можете брать больше конфет чем осталось в куче, а в ней всего {lot_candy} конфет. Попробуйте еще раз')
        return game_play_human(name1, name2, lot_candy, taken_candies)
    
    lot_candy = lot_candy - temp
    if lot_candy == 0:
        print(f'Поздравляю! {name} - забирает всю кучу конфет')
        sys.exit()
    else:
        name1 = name2
        name2 = name
        return game_play_human(name1, name2, lot_candy, taken_candies)

def game_play_bot(name1, name2, lot_candy, taken_candies):
    ''' Игра с ботом '''

    name = name1
    if name == 'Бот':
        temp = random.randint(1, taken_candies)
        print(f'{name} взял из кучи {temp} конфет(ы)')
    else:    
        temp = input(f'{name} в куче {lot_candy} конфет. Сколько из них Вы возьмете?  ')
        if (not temp.isdigit()):
            print ('Вы ввели что-то не то. Попробуйте еще раз')
            return game_play_bot(name1, name2, lot_candy, taken_candies)
        temp = int(temp)
        if temp == 0:
            print ('Вы должны взять хотя бы одну конфету. Попробуйте еще раз')
            return game_play_bot(name1, name2, lot_candy, taken_candies)
        elif temp > taken_candies:
            print (f'Вы не можете брать больше конфет чем: {taken_candies}. Попробуйте еще раз')
            return game_play_bot(name1, name2, lot_candy, taken_candies)
        elif temp > lot_candy:
            print (f'Вы не можете брать больше конфет чем осталось в куче, а в ней всего {lot_candy} конфет. Попробуйте еще раз')
            return game_play_bot(name1, name2, lot_candy, taken_candies)
    lot_candy = lot_candy - temp
    if lot_candy == 0:
        print(f'Поздравляю! {name} - забирает всю кучу конфет')
        sys.exit()
    else:
        name1 = name2
        name2 = name
        return game_play_bot(name1, name2, lot_candy, taken_candies)

def game_play_smart_bot(name1, name2, lot_candy, taken_candies, count, game_move):
    ''' Игра с умным ботом '''

    name = name1
    count += 1
    if name == 'Умный Бот': # Все еще тупой бот
        temp = random.randint(1, taken_candies)
        print(f'{name} взял из кучи {temp} конфет(ы)')
    else:    
        temp = input(f'{name} в куче {lot_candy} конфет. Сколько из них Вы возьмете?  ')
        if (not temp.isdigit()):
            print ('Вы ввели что-то не то. Попробуйте еще раз')
            return game_play_smart_bot(name1, name2, lot_candy, taken_candies, count, game_move)
        temp = int(temp)
        if temp == 0:
            print ('Вы должны взять хотя бы одну конфету. Попробуйте еще раз')
            return game_play_smart_bot(name1, name2, lot_candy, taken_candies, count, game_move)
        elif temp > taken_candies:
            print (f'Вы не можете брать больше конфет чем: {taken_candies}. Попробуйте еще раз')
            return game_play_smart_bot(name1, name2, lot_candy, taken_candies, count, game_move)
        elif temp > lot_candy:
            print (f'Вы не можете брать больше конфет чем осталось в куче, а в ней всего {lot_candy} конфет. Попробуйте еще раз')
            return game_play_smart_bot(name1, name2, lot_candy, taken_candies, count, game_move)
    lot_candy = lot_candy - temp
    game_move = temp
    if lot_candy == 0:
        print(f'Поздравляю! {name} - забирает всю кучу конфет')
        sys.exit()
    else:
        name1 = name2
        name2 = name
        return game_play_smart_bot(name1, name2, lot_candy, taken_candies, game_move)

print("*" * 10, " Игра забери всю кучу конфет для двух игроков, или для игрока и бота ", "*" * 10)
start_game()
