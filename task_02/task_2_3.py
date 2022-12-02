import os

from random import randint

os.system('cls')

def ask_number():
    number = input('Введите размер массива   ')
    if (not number.lstrip('+-').isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()
    number = int(number)
    if(number < 1):
        print('Число должно быть больше нуля. Попробуйте еще раз')
        return ask_number()
    return number

def ask_array(array):
    for i in array:
        if i<0:
            array.insert(array.index(i)+1, 0)
    return array

n = ask_number()
array = [randint(-99,99) for _ in range(n)]

print(f'пусть N = {n}, тогда {array} => {ask_array(array)}')