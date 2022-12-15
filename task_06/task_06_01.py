import os
import re
os.system('cls' if os.name=='nt' else 'clear')

def input_list():
    list_1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
    l_1 = "qwe"
    list_2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
    l_2 = "йцу"
    list_3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
    l_3 = "йцу"
    list_4 = ["123", "234", 123, "567"]
    l_4 = "123"
    list_5 = []
    l_5 = "123"
    print(f'Перед Вами пять вариантов\n1. В списке {list_1} найти строку {l_1}\n2. В списке {list_2} найти строку {l_2}\n3. В списке {list_3} найти строку {l_3}\n4. В списке {list_4} найти строку {l_4}\n5. В списке {list_5} найти строку {l_5}\n')
    temp = input('Выберите любой вариант нажав цифру от 1 до 5  ')
    if not re.match(r'^[1-5]$', temp):
        print('Вы ввели что-то не то. Попробуйте еще раз.')
        return input_list()
    elif temp == '1':
        result_list, resalt_l = list_1, l_1
    elif temp == '2':
        result_list, resalt_l = list_2, l_2
    elif temp == '3':
        result_list, resalt_l = list_3, l_3
    elif temp == '4':
        result_list, resalt_l = list_4, l_4
    elif temp == '5':
        result_list, resalt_l = list_5, l_5
    return result_list, resalt_l    

result_list, resalt_l = input_list()
ls = -1 if result_list.count(resalt_l) < 2 else list(filter(lambda x: x[1] == resalt_l, enumerate(result_list)))[1][0]
print(f'{result_list} => {ls}')