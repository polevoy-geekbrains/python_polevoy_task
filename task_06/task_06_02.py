import os
import math
import random

os.system('cls' if os.name=='nt' else 'clear')


ls = random.sample(range(50), random.randint(5,10))
center = math.ceil(len(ls)/2)
left = ls[:center]
right = ls[center:]
right.reverse()

result = list(map(lambda tuple: tuple[0]*tuple[1], zip(left,right)))
print(f'{ls} => {result}')