# 1. Ваша задача написать программу, принимающее число - номер кредитной карты
# (число может быть четным или не четным). И проверяющей может ли такая карта существовать.
# Предусмотреть защиту от ввода букв, пустой строки и т.д.
# По алгоритму луна
# Примеры:
# validate(4561261212345464) #=> False
# validate(4561261212345467) #=> True

def is_number(num: str) -> bool:
    if not num:
        print('Вы ничего не ввели!')
        return False
    else:
        if not num.isdigit():
            print(f'Можно вводить только цифры, Вы ввели {card_input}')
        else:
            return num.isdigit()


def logic(array, el):
    res = 0
    if el * 2 > 9:
        res = el * 2 - 9
    else:
        res = el * 2
    array.append(res)
    return array


def validation(card_number):
    card_number_list = []
    modify_list = []
    sum_card_number_list = 0

    for el in card_number:
        card_number_list.append(int(el))

    control_num = card_number_list[-1]
    card_number_list.pop(-1)
    even = card_number_list[1::2]
    odd = card_number_list[0::2]

    if len(card_number_list) % 2 == 0:
        for el in even:
            logic(modify_list, el)
        sum_card_number_list = sum(modify_list) + sum(odd)
    elif len(card_number_list) % 2 != 0:
        for el in odd:
            logic(modify_list, el)
        sum_card_number_list = sum(modify_list) + sum(even)

    sum_numbers = sum_card_number_list + control_num

    if sum_numbers % 10 == 0:
        return True
    else:
        return False


while True:
    card_input = input('Введите номер карты: ')
    just_numbers = is_number(card_input)
    if just_numbers:
        valid_or_invalid = validation(card_input)
        if valid_or_invalid:
            print('Valid')
            break
        else:
            print('Invalid')

# 2.На вход подается строка, например, "cccbba" результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"


def number_of_letters(word):
    array = {}
    str1 = ''
    for el in word:
        array[el] = word.count(el)
    for k in array.keys():
        if array[k] == 1:
            str1 += k
        else:
            str1 += k + str(array[k])
    print(str1)


number_of_letters('aaabbbcccdddeeele')

# 3.Калькулятор
# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Проверка деления на 0.
#
# Пример
# Выберите операцию:
#     1. Сложение
#     2. Вычитание
#     3. Умножение
#     4. Деление
# Введите номер пункта меню:
# >>> 4
# Введите первое число:
# >>> 10
# Введите второе число:
# >>> 3
# Частное: 3, Остаток: 3


def calculator():
    print("Выберите действие, которое хотите сделать:\n"
          "1.Сложение\n"
          "2.Вычитание\n"
          "3.Умножение\n"
          "4.Деление\n")
    options = ('1', '2', '3', '4')
    user_option = input("Введите номер пункта меню:")
    if user_option not in options:
        print('Введите только пункт меню от 1 до 4!')
    else:
        x = float(input("Введите первое число:"))
        y = float(input("Введите второе число:"))
        if user_option == '1':
            print(x + y)
        elif user_option == '2':
            print(x - y)
        elif user_option == '3':
            print(x * y)
        elif user_option == '4':
            if y == 0:
                print("На ноль делить нельзя!")
            elif y != 0 and x % y == 0:
                print(x / y)
            elif y != 0 and x % y != 0:
                division = x / y
                str_division = str(division)
                quotient = str_division.split(".")[0]
                remainder = str_division[str_division.find(".") + 1:]
                remainder_1 = remainder[0]
                print(f"Частное: {quotient}, остаток: {remainder_1}")


while True:
    calculator()
