# ПРАКТИЧЕСКОЕ ЗАДАНИЕ К УРОКУ 6 #
______
## Данные, функции и модули в Python. Продолжение ##
----------
### 1 ###
Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
Примеры
список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
список: [], ищем: "123", ответ: -1

### 2 ###
Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

### 3 ###
Сформировать список из N членов последовательности.
Для N = 5: 1, -3, 9, -27, 81 и т.д.

### 4 ###
Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

### 5 ###
Есть список случайных чисел в промежутке от 1 до 100, количеством 200. Создайте список кортежей, первый элемент которого - индекс элемента, а второй - сам элемент, при условии, что они не совпадают.
[1,1,1,1] -> [(0,1),(1,1),(2,1),(3,1)] -> [(0,1),(2,1),(3,1)]

### 6 ###
Из списка выше оставьте только те пары, где сумма кортежа кратна 5
Пример
[(10,25),(3,4),(4,1)] => [(10,25),(4,1)]


__Нужно решить задачи с помощью лямбд, filter, map, zip, enumerate, list comprehension__


