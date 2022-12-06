import os

os.system('cls')

def ask_number():
    number = input(f'Введите число. Число должно быть целым   ')
    if (not number.lstrip('+-').isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()
    number = int(number)
    return number

def binary_number(number):
    '''Используется функция binary_number(number) для преобразования десятичного числа в двоичное 
            Параметр (number) - Целое число.
        Функция преобразовывает десятичное число в строковую запись двоичного числа.
        Для обозначения отрицательных чисел используется прямой код (подстановка еденицы в начало) 
            Возвращаемое значение: 
                        binary_number = строка вида 1011 или 1 1011 количество знаков не ограничено  \n'''
    if number < 0:
        number = number * -1
        binary_number = ''
        while number != 0:
            binary_number = str(number%2) + binary_number
            number = number // 2
        binary_number = str('1 ') + binary_number
    else:
        binary_number = ''
        while number != 0:
            binary_number = str(number%2) + binary_number
            number = number // 2
    return binary_number
    
N = ask_number()
print(binary_number.__doc__)
print(f'{N} -> {binary_number(N)}')