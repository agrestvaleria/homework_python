# 1. Создайте программу, которая, принимая массив имён, возвращает строку
# описывающая количество лайков (как в Facebook).
#
# Примеры:
# likes() -> "no one likes this"
# likes("Ann") -> "Ann likes this"
# likes("Ann", "Alex") -> "Ann and Alex like this"
# likes("Ann", "Alex", "Mark") -> "Ann, Alex and Mark like this"
# likes("Ann", "Alex", "Mark", "Max") -> "Ann, Alex and 2 others like this"

array = ['Ann, Tim', 'Alex', 'Katty', 'Paul']


def likes(arr):
    if len(arr) == 0:
        print('no one likes this')
    elif len(arr) == 1:
        print(f'{arr[0]} likes this')
    elif len(arr) == 2:
        print(f'{arr[0]} and {arr[1]} like this')
    elif len(arr) == 3:
        print(f'{arr[0]}, {arr[1]} and {arr[2]} like this')
    elif len(arr) > 3:
        count = len(arr) - 2
        print(f'{arr[0]}, {arr[1]} and {count} others like this')


likes(array)


# 2. Напишите программу, которая перебирает последовательность от 1 до 100.
# Для чисел кратных 3 она должна написать: "Fuzz" вместо печати числа,
# а для чисел кратных 5  печатать "Buzz".
# Для чисел которые кратны 3 и 5 надо печатать "FuzzBuzz". Иначе печатать число.

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)


# 3. В классическом варианте игра рассчитана на двух игроков.
# Каждый из игроков задумывает и записывает тайное 4-значное число с неповторяющимися цифрами.
# Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями в тайном числе
# (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"
# Пример
# Загадано число 3219
# >>> 2310
# Две коровы, один бык
# >>> 3219
# Вы выиграли!

number = 3219
new_number = input('Введите четырехзначное число: ')
number_str = str(number)

bik = 0
korova = 0
unique = set(list(new_number))


if len(new_number) == 0:
    print('Вы ничего не ввели!')
else:
    if not new_number.isdigit():
        print('Введите только цыфры!')
    elif len(new_number) != 4:
        print('Вы ввели не четырехзначное число!')
    elif len(set(number_str)) != len(unique):
        print('Цыфры не должны повторяться!')
    else:
        for i in number_str:
            if i in new_number:
                if number_str.index(i) == new_number.index(i):
                    bik += 1
                else:
                    korova += 1

        answer = ''

        if bik > 0 or korova > 0:
            if korova == 1:
                answer += 'Одна корова'
            elif korova == 2:
                answer += 'Две коровы'
            elif korova == 3:
                answer += 'Три коровы'
            elif korova == 4:
                answer += 'Четыре коровы'

            if len(answer) > 0 and 0 < bik < 4:
                answer += ', '

            if bik == 1:
                answer += 'один бык'
            elif bik == 2:
                answer += 'два быка'
            elif bik == 3:
                answer += 'три быка'
            elif bik == 4:
                answer += 'Вы победили!'

            print(answer)

        else:
            print('Мимо!')
