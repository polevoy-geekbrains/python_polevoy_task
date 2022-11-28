import os

os.system('cls')

def enter_dey_of_week():
    dey_of_week = input('Введите день недели числом от 1 до 7  ')
    if (not dey_of_week.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return enter_dey_of_week()
    dey_of_week = int(dey_of_week)
    if(dey_of_week < 1 or dey_of_week > 7):
        print('День недели должен быть от 1 до 7. Попробуйте еще раз')
        return enter_dey_of_week()
    return dey_of_week
dey_of_week = enter_dey_of_week()
if(5<dey_of_week<8):
    print(f'{dey_of_week} -> выходной день')
else:
    print(f'{dey_of_week} -> рабочий день')
