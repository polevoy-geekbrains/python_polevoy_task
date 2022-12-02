import os

os.system('cls')

def ask_number():
    number = input('Введите целое положительное число   ')
    if (not number.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()
    number = int(number)
    if(number < 1):
        print('Число должно быть больше нуля. Попробуйте еще раз')
        return ask_number()
    return number

def factorial(number):
    i = 1
    result = []
    for j in range(1, number+1):
        i *= j
        result.append(i)
    return result

N = ask_number()
print(f'пусть N = {N}, тогда {factorial(N)}')