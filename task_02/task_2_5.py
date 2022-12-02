import os
import time

os.system('cls')

def ask_number(name):
    number = input(f'Введите {name} диапазона случайных чисел. Число должно быть целым   ')
    if (not number.lstrip('+-').isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number(name)
    number = int(number)
    return number

def rand_int(min, max):
    t = time.time()
    t = t - float(str(t).split('.')[0])
    r = min + t * (max - min)
    return int(r)

min = ask_number('начало')
max = ask_number('конец')
result = rand_int(min, max)
print(f'Случайное число в диапазоне от {min} до {max}: {result}')