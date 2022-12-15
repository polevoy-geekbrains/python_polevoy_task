import os
os.system('cls' if os.name=='nt' else 'clear')
import random


random_nums = [random.randint(1, 100) for _ in range(200)]
b = list(filter(lambda x: (x[0] + x[1]) % 5 == 0, enumerate(random_nums)))
print(f'Список кортежей, по условиям пятого задания, если сума элементов кортежа кратна пяти {b}')