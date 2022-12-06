import os
import math
import re

os.system('cls')

def ask_list():
    str_list = input('Введите числа через пробел: ').split(' ')
    number_list = []
    for val in str_list:
        if re.match(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", val):
            number_list.append(float(val))
        else:
            print('Вы ввели что-то не то попробуйте еще раз')
            return ask_list()
    return number_list

def mult_list(number_list):
    mult_list = []
    length = len(number_list)
    for i in range(math.ceil(length/2)):
        mult_list.append(number_list[i]*number_list[length-i-1])
    return mult_list

num = ask_list()
print(f'{num} => {mult_list(num)}')