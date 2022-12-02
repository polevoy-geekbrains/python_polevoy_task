import os

os.system('cls')

import re

def ask_number():
    number = input('Введите число  ')
    if re.match(r"^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$", number):
         number = float(number)
         return number
    else:
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()

def sum_numbers(number):
    sum = 0
    if float(number) < 0:                            
       number = float(number) * (-1)  
    for i in str(number):
        if i != ".":
           sum += int(i)
    return sum

number = ask_number()
print(f'{number} -> {sum_numbers(number)}')