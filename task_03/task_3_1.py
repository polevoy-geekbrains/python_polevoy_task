import os

from random import randint

os.system('cls')

def ask_number():
    number = input('Введите количество чисел в списке   ')
    if (not number.lstrip('+-').isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()
    number = int(number)
    if(number < 1):
        print('Число должно быть больше нуля. Попробуйте еще раз')
        return ask_number()
    return number

def ask_sum(array):
    sum = 0
    for i, val in enumerate(array):
        if i%2 != 0:
            sum += val
    return sum

n = ask_number()
array = [randint(-99,99) for _ in range(n)]

print(f'Список чисел: {array} => Сумма элементов находящихся на нечетных позициях = {ask_sum(array)}')