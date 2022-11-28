import os

os.system('cls')

import re

def ask_coordinate(name):
    coordinate = input(f'Введите координаты точки {name}. Важно! {name} ≠ 0  ')
    if re.match(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", coordinate):
        coordinate = float(coordinate)
    else:
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_coordinate(name)
    if(coordinate == 0):
        print(f'Внимание, координата {name} не должна быть равна 0. Попробуйте еще раз')
        return ask_coordinate(name)
    return coordinate

def number_of_quarter(x,y):
    if x > 0 and y > 0:
        return 'I' 
    elif x < 0 and y > 0:
        return 'II'
    elif x < 0 and y < 0:
        return 'III'
    else:
        return 'VI'

x = ask_coordinate('X')
y = ask_coordinate('Y')
quarter = number_of_quarter(x,y)
print (f'Точка с координатами X({x}) и Y({y}) находится в {quarter} четверти')