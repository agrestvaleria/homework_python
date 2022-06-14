# 1. Напишите функцию, которая принимает на вход одномерный массив и два числа -
# размеры выходной матрицы. На выход программа должна подавать матрицу нужного размера,
# сконструированную из элементов массива.
# reshape([1, 2, 3, 4, 5, 6], 2, 3) =>
# [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# reshape([1, 2, 3, 4, 5, 6, 7, 8,], 4, 2) =>
# [
#     [1, 2],
#     [3, 4],
#     [5, 6],
#     [7, 8]
# ]

def reshape(list_1: list, num_1: int, num_2: int) -> list:
    array = []
    for i in range(num_1):
        while len(list_1) > num_2:
            part = list_1[:num_2]
            array.append(part)
            list_1 = list_1[num_2:]
        array.append(list_1)
        return array


print(reshape([1, 2, 3, 4, 5, 6, 7, 8], 4, 2))

# 2. Генераторы:
#     1) Напишите генератор который принимает список numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
#     и возвращает новый список только с положительными числами
#     2) Необходимо составить список чисел которые указывают на длину слов в строке:
#     sentence = " thequick brown fox jumps over the lazy dog", но только если слово не "the".

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
number_plus = [x for x in numbers if x >= 0]
print(number_plus)

sentence = 'thequick brown fox jumps over the lazy dog'
length_of_words = [len(x) for x in sentence.split() if x != ' the ']
print(length_of_words)

# 3. Шифр Цезаря — один из древнейших шифров.
# При шифровании каждый символ заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
#
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.

def logic(i, num, option, alphabet):
    position = alphabet.find(i)
    new_position = 0
    if option == "encode":
        new_position = position + num
    elif option == "decode":
        new_position = position - num
    return alphabet[new_position]


def encode_decode(str1: str, num: int, option: str):
    """""
    Основное задание + 3 пункта в бонусных очках
    """""
    alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ' \
                  'abcdefghijklmnopqrstuvwxyz'
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРС' \
                  'ТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    result = ''
    for i in str1:
        if i in alphabet_ru:
            result += logic(i, num, option, alphabet_ru)
        elif i in alphabet_en:
            result += logic(i, num, option, alphabet_en)
        else:
            result += i
    return result


print(encode_decode('hello world!', 3, 'encode'))
print(encode_decode('ymnx Nx f yjXy xyWnsl', 5, 'decode'))
