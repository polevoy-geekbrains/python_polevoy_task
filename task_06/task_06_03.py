import os

os.system('cls' if os.name=='nt' else 'clear')

def enter_number():
    number = input('Введите N членов последовательности  ')
    if (not number.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return enter_number()
    elif int(number) > 1024:
        print('N должен быть < 1024. Попробуйте еще раз')
        return enter_number()
    else:
        return int(number)


c = list(map(lambda i: ((-3)**i), [i for i in range(enter_number())]))
print(c)