import os
os.system('cls' if os.name=='nt' else 'clear')
import random


random_nums = [random.randint(1, 100) for _ in range(200)]
b = list(filter(lambda x: x[0] != x[1], enumerate(random_nums)))
print(f'Список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают {b}')
# c = list(filter(lambda x: x[0] == x[1], enumerate(random_nums)))
# a = list(enumerate(random_nums))
# print(a)
# print(c)
# Я не стал убирать общий список кортежей и список кортежей элементы которго совпадают, так как они удобны при проверке результата. 

