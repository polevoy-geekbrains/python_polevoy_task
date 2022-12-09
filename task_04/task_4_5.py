import os

# очищаем консоль
os.system('cls')

def decode(st: str):
    ''' Функция RLE восстановления
        Args:
         st: str - строка сжатая методом RLE
         Input:
         ()
         Reterns:
          res: str  - восстановленная строка '''
    count = ''
    res = ''
    for i in st:
        if i.isdigit():
            count += i
        else:
            res += i * int(count)
            count = ''
    return res

def encode(st: str):
    ''' Функция RLE сжатия
        Args:
         st: str - строка для сжатия 
         Input:
         ()
         Reterns:
          res: str  - сжатая методом RLE строка st '''
    res = ''
    c = st[0]
    count = 0
    for ch in st:
        if(ch == c):
            count+=1
        else:
            res += str(count) + c
            c = ch
            count = 1
    res += str(count) + c
    return res

def convert_file(f_convert: callable, input_file: str, output_file: str, conversion_type: str):
    '''Функция чтения и записи файлов. Запрашивает функцию для обработки данных файла,
        выводит на печать результаты чтения и записи.
        Args:
         (f_convert: callable - внешняя функция для обработки данных из файла,
          input_file: str - файл из которого осуществляется чтение данных,
          output_file: str, - файл в который записываюся обработанные данные,
          conversion_type: str - название типа обработки данных, используется для подсказки 
         Input:
          ()
         Reterns:
          print() - информация о считанных и записанных данных и именах файлов
          output_file - файл с записанными данными (если уже имеется, то данные перезаписываются) '''
    data = ''
    with open(input_file, 'r') as f:
        data = f.read()
        print(f'Содержимое файла ({input_file}): {data}\n')
    data = f_convert(data)
    with open(output_file, 'w') as f:
        f.write(data)
        print(f'Результат {conversion_type}: {data} записан в файл: ({output_file}): \n')

convert_file(encode,'rle_data.txt','rle_encode.txt', 'сжатия') # файлы rle_data.txt и rle_encode.txt должны находится в одной папке с программой
convert_file(decode,'rle_encode.txt', 'rle_decode.txt', 'восстановления') # файлы rle_encode.txt и rle_decode.txt должны находится в одной папке с программой