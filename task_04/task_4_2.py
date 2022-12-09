import os
import time
import re

os.system('cls')

def homework():
    '''    Задание № 2 
    
        Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
Постарайтесь решить за одно условие
[1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4] \n '''
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

def result_namber_list(number_list):
    result_list = []
    for i in number_list:
        if i not in result_list:
            result_list.append(i)
    return result_list

number_list = ask_list()
print(f'\n {number_list} -> {result_namber_list(number_list)}')