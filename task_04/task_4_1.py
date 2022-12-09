import os
import time

os.system('cls')

def homework():
    '''    Задание № 1 
    
        Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
N = 20 -> [2,5]
N = 30 -> [2, 3, 5] \n '''
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

def ask_number():
    ''' Запрашивает ввод натурального числа. Проверяет является ли
         введенное значение натуральным числом и возвращает натуральное число.

         Args:
         () 
         Input:
          str - ввод числа с консоли
         Reterns:
          int - натуральное число '''
    number = input(f'Введите натуральное число N: ')
    if(not number.isdigit()):
        print('Ошибка: вы ввели что-то не то! Повторите ввод')
        return ask_number()
    number = int(number)
    if(number <= 0):
        print(f'Ошибка! Число должно быть больше 0')
        return ask_number()
    return number

def prime_factor(N):
    ''' Принимает натуральное число. Возвращает список простых множителей введенного числа
        Args:
         int - натуральное число
         Input:
          ()
         Reterns:
          list - список натуральных множителей '''
    
    prime_numbers = []
    for i in range(2,N+1):
        while not N % i:
            if not prime_numbers.count(i):
                prime_numbers.append(i)
            N //= i
        i += 1 
    return prime_numbers
    

N = ask_number()
print(f'N = {N} -> {prime_factor(N)}')