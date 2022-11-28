import os

os.system('cls')

def ask_quarter():
    quarter = input('Введите номер четверти координатной плоскости. Номер вводится цифрами от 1 до 4   ')
    if (not quarter.isdigit()):
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return ask_quarter()
    quarter = int(quarter)
    if(quarter < 1 or quarter > 4):
        print('Номер четверти должен быть от 1 до 4. Попробуйте еще раз')
        return ask_quarter()
    return quarter
def coordinates_of_quarter(quarter):
    if quarter == 1:
        return 'quarter = 1 => x∈(0,∞) u y∈(0,∞)' 
    elif quarter == 2:
        return 'quarter = 2 => x∈(0,∞) u y∈(0,-∞)'
    elif quarter == 3:
        return 'quarter = 3 => x∈(0,-∞) u y∈(0,-∞)'
    else:
        return 'quarter = 4 => x∈(0,-∞) u y∈(0,∞)'

quarter = ask_quarter()
coordinates = coordinates_of_quarter(quarter)
print(f'{coordinates}')
