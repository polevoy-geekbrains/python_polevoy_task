import os

os.system('cls')

print('X | Y | Z | истинность ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z ')
print('  |   |   | ')
for X in range(0,2):
    for Y in range(0,2):
        for Z in range(0,2):
            a = not(X|Y|Z)
            b = not X and not Y and not Z
            print(f'{X} | {Y} | {Z} |               {a == b}')