import os
import re
import time

os.system('cls')

def homework():
    '''    Задание № 3 
    
        Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
        между максимальным и минимальным значением дробной части элементов.
        Пример:
            [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
            [4.07, 5.1, 8.2444, 6.9814] - 0.9114 или 9114 \n '''
    number = input('Сколько еще секунд Вы хотите видеть описание задачи?   ')
    if (not number.lstrip('+-').isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return homework()
    number = int(number)
    if(number < 0):
        print('Число секунд не может быть отрицательным. Попробуйте еще раз')
        return homework()
    return number

print(homework.__doc__)
time_sleep = homework() 
time.sleep(time_sleep)
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

def float_list(number_list):
    float_list = []
    length = len(number_list)
    for i in range(length):
        if number_list[i] < 0:
            number_list[i] = number_list[i] * -1
        float_list.append(number_list[i] % 1)
    return float_list

def max_min(float_list):
    num_max = max(float_list)
    num_min = min(float_list)
    diff = round((num_max - num_min),10)
    return diff

def get_float_list(fsum):
    strnum = str(fsum)
    return int(strnum[strnum.index('.')+1:])

nums = ask_list()
fractional_list = float_list(nums)
diff = max_min(fractional_list)

print(f'{nums} => {diff} или {get_float_list(diff)}')