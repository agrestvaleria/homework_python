# 1. Напишите декоратор, который проверял бы тип параметров функции, конвертировал их если надо и складывал:
#
# @typed(type=’str’)
# def add_two_symbols(a, b):
#     return a + b
#
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> "55"
# add_two_symbols('a', 'b') -> 'ab’
#
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
#     return a + b + с
#
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(type):
    def decorator(func):
        def wrapper(*args):
            float_list = []
            str_list = []
            if type == 'int':
                for el in args:
                    float_list.append(float(el))
                return func(*float_list)
            if type == 'str':
                for el in args:
                    str_list.append(str(el))
                return func(*str_list)
        return wrapper
    return decorator


@typed(type='int')
def add_three_symbols(a, b, c):
    return a + b + c


print(add_three_symbols("3", 5, 0))


@typed(type='str')
def add_two_symbols(a, b):
    return a + b


print(add_two_symbols("3", 5))

# 2. На вход подаётся некоторое количество (не больше сотни) разделённых пробелом целых чисел (каждое не меньше 0 и не больше 19).
# Выведите их через пробел в порядке лексикографического возрастания названий этих чисел в английском языке.
# Т.е., скажем числа 1, 2, 3 должны быть выведены в порядке 1, 3, 2,
# поскольку слово two в словаре встречается позже слова three, а слово three -- позже слова one (иначе говоря, поскольку выражение 'one' < 'three' < 'two' является истинным)
# number_names = {
#     	0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
#     	10: 'ten', 11: 'eleven', 12: 'twelve',
#     	13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',  18: 'eighteen', 19: 'nineteen'}

def decorator(func):
    def wrapper(arg1):
        number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                        5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
                        10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen',
                        14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
                        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        sorted_values = sorted(number_names.values())
        sorted_number_names = {}
        list_int_args = [int(i) for i in arg1.split(' ')]
        sorted_args = []
        for i in sorted_values:
            for k in number_names.keys():
                if number_names[k] == i:
                    sorted_number_names[k] = number_names[k]
                    break
        for k in sorted_number_names.keys():
            for i in list_int_args:
                if k == i:
                    sorted_args.append(i)
        list_str_args = [str(i) for i in sorted_args]
        print(' '.join(list_str_args))
        func(arg1)
    return wrapper


def valid_numbers(num: str):
    if not num:
        print('Вы ничего не ввели!')
        return False
    for i in num:
        if i not in '0123456789 ':
            print('Только положительные цифры и пробел')
            return False
    num_list = [int(i) for i in num.split(' ')]
    if len(num_list) > 100:
        print('Нельзя вводить более 100 чисел!')
        return False
    for i in num_list:
        if i > 19:
            print('Числа должны быть не меньше 0 и не больше 19!')
            return False
    else:
        return True


while True:
    user_input = input('Введите последовательность чисел: ')
    is_valid = valid_numbers(user_input)
    if not is_valid:
        continue
    else:
        function_decorated = decorator(valid_numbers)
        function_decorated(user_input)
        break
