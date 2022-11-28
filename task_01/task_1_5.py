import os

os.system('cls')

import re

def ask_coordinate(name):
    coordinate = input(f'Введите {name}.  ')
    if re.match(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", coordinate):
        coordinate = float(coordinate)
    else:
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_coordinate(name)
    return coordinate
x1 = ask_coordinate('x координату точки A')
y1 = ask_coordinate('y координату точки A')
x2 = ask_coordinate('x координату точки B')
y2 = ask_coordinate('y координату точки B')
distance = round(((x1 - x2)**2 + (y1 - y2)**2)**0.5, 2)
print(f'A ({x1}, {y1}); B ({x2}, {y2}) -> {distance}')