import os

os.system('cls')

alphabet_ru = "абвг.деёж;зийА:БВГДкл,мн?опЕЁЖЗрстуфхИЙКЛ!МНцчшщУФХЦЧъыьэШЩюя ЭЮЯОПРСТ"

def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]

def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:        
        return symbols[(index - n) % len(symbols)]

def encrypt(text, n = 3):
    res = ""
    for i in range(0, len(text)): 
        res += shift(text[i], alphabet_ru, n)
    return res

def decrypt (text,):
    res = ""
    n = input('Введите ключ для декодирования текста (рекомендую ввести 3)  ')
    n = int(n)              
    for i in range(0, len(text)):
        res += back_shift(text[i], alphabet_ru, n)
    return res

def input_world():
    str = encrypt(input("Введите слова для кодирования. Слова должны быть на русском языке: "))
    print(f'Закодированный вариант: {str}')
    decrypt_str = decrypt(str)
    print(f'Раскодированный вариант: {decrypt_str}')

def input_text(f_convert: callable, input_file: str, output_file: str, conversion_type: str):
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
    with open(input_file, 'r', encoding='utf-8') as f:
        data = f.read()
        print(f'Содержимое файла ({input_file}):  {data}\n')
    data = f_convert(data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(data)
        print(f'Результат {conversion_type}:  {data}    Результат записан в файл: ({output_file}): \n')


def digit_selection():
    a = input('Сделайте выбор, что собираетесь кодировать: Если слово введеное с клавиатуры, нажмите 1  Если текст из файла нажмите 2    ') 
    if a == '1':
        input_world()
    elif a == '2':
        input_text(encrypt,'cezar_data.txt','cezar_encode.txt', 'кодирования') # файлы rle_data.txt и rle_encode.txt должны находится в одной папке с программой
        input_text(decrypt,'cezar_encode.txt', 'cezar_decode.txt', 'восстановления') # файлы rle_enc
    else:
        print ('Вы ввели что-то не то. Попробуйте еще раз')
        return digit_selection()

digit_selection = digit_selection() 