import os

os.system('cls') # Очистка консоли

def ask_number():
    '''Используется функция ask_number() для ввода числа и его проверки на натуральность
            Параметры отсутствуют.
            Внутри функции осуществляется однократный ввод с клавиатуры.
            Если число не натуральное (или равно 0) предлагается повторить ввод
        Возвращаемое значение:
                        number = Натуральное число. '''
    number = input('Введите целое положительное число   ') # Вводим число
    if (not number.isdigit()): # Проводим проверку ввода если в числе есть любые знаки кроме цифр просим повторить ввод.
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_number()
    number = int(number) # Определяем число как int
    if(number < 1): # Снова проводим проверку ввода если введен 0 просим повторить ввод.
        print('Число должно быть больше нуля. Попробуйте еще раз')
        return ask_number() 
    
    return number # Возвращаем натуральное число 

def list_negafib(n):
    '''Используется функция list_negafib(n) для создания списка негафибоначчи
            Параметр (n) - Натуральное число, ограничивающее список чисел Фибоначчи
                Функция составляет список чисел Фибоначчи, в том числе для отрицательных индексов ограниченное Параметром
        Возвращаемое значение  (например для 8): 
                        list_negafib = список чисел вида [-21 ,13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]\n'''
    list_negafib = []
    previous = 0
    next = 1
    list_negafib.append(next)
    for i in range(1, n):
        sum = previous - next
        previous = next
        next = sum
        list_negafib.append(sum)

    list_negafib.reverse()

    previous = 0
    next = 1
    list_negafib.append(previous)
    list_negafib.append(next)
    for i in range(1, n):
        sum = previous + next
        previous = next
        next = sum
        list_negafib.append(sum)
    
    return list_negafib # Возвращаем итоговый список негафибоначчи

N = ask_number()

print(ask_number.__doc__)
print(list_negafib.__doc__)
print(f'для k = {N} список будет выглядеть так: {list_negafib(N)}')