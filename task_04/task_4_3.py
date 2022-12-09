import os
import time

os.system('cls')

def homework():
    '''    Задание № 3 
    
        В файле, содержащем фамилии студентов и их оценки, изменить на буквы
        в верхнем регистре тех студентов, которые имеют средний балл более «4».
Нужно перезаписать файл.
Пример:
Ангела Меркель 5
Энакин Скайуокер 5
Фредди Меркури 3
Александр Пушкин 4 \n '''
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

from typing import List

def list_changed(spisok: List[str], accept: str) -> str:
    list_file = ''
    for student in spisok:
        if student.count(accept):
            student = student.upper()
        string = student + "\n"
        list_file += string
    return list_file


students_list = open('students.txt', 'r', encoding='utf-8')
new_list = students_list.read().split('\n')
students_list.close()

rewriten_list = list_changed(new_list, accept = '5')


students_list = open('students.txt', 'w', encoding='utf-8')
students_list.write(rewriten_list)
students_list.close()