# 1. Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" =>
# ["I", "love", "arrays", "they", "are", "my", "favorite"]

a = "Robin Singh"
print(a.split())
b = "I love arrays they are my favorite"
print(b.split())

# 2.Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”

a = ['Ivan', 'Ivanou']
b = 'Minsk'
c = 'Belarus'
a1 = ' '.join(a)
print(f'Привет, {a1}! Добро пожаловать в {b} {c}')

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"

a = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(a))

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6

a = [4, 8, -10, 559, -80, 36, 'sea', 'sky', {'1': 2}, 888]
a.insert(3, 300)
del a[6]
print(a)

# 5. Есть 2 словаря
# a = { 'a': 1, 'b': 2, 'c': 3}
# b = { 'c': 3, 'd': 4,'e': 5}
#
# Необходимо их объединить по ключам, а значения ключей поместить в список,
# если у одного словаря есть ключ "а", а у другого нету, то поставить значение
# None на соответствующую позицию(1-я позиция для 1-ого словаря,
# вторая для 2-ого)
# ab = {'a': [1, None], 'b': [2, None], 'c': [3, 3], 'd': [None, 4],
# 'e': [None, 5]}

# 1 вариант
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'c': 3, 'd': 4, 'e': 5}
dict3 = {}

for key in dict1.keys():
    if key in dict2:
        dict3[key] = [dict1[key], dict2[key]]
    else:
        dict3[key] = [dict1[key], 'None']

for key in dict2.keys():
    if key in dict1:
        dict3[key] = [dict2[key], dict1[key]]
    else:
        dict3[key] = ['None', dict2[key]]

print(dict3)

# 2 вариант
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': 5}
q = {q: [a.get(q, None), b.get(q, None)] for q in sorted(set(a) | set(b))}
print(q)

# 6. Вам передан массив чисел. Известно, что каждое число в этом массиве имеет
# пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

a = [1, 5, 2, 9, 2, 9, 1]
print(min(a, key=a.count))

# 7. Дан текст, который содержит различные английские буквы и знаки препинания.
# Вам необходимо найти самую частую букву в тексте.
# Результатом должна быть буква в нижнем регистре.
# При поиске самой частой буквы, регистр не имеет значения,
# так что при подсчете считайте, что "A" == "a".
# Убедитесь, что вы не считайте знаки препинания, цифры и пробелы, а только буквы.
# Если в тексте две и больше буквы с одинаковой частотой,
# тогда результатом будет буква, которая идет первой в алфавите.
# Для примера, "one" содержит "o", "n", "e" по одному разу, так что мы выбираем "e".
#
# "a-z" == "a"
# "Hello World!" == "l"
# "How do you do?" == "o"
# "One" == "e"
# "Oops!" == "o"
# "AAaooo!!!!" == "a"
# "a" * 9000 + "b" * 1000 == "a"

str1 = 'How do you do?'
lower_string = str1.lower()
letters = ''.join(filter(str.isalpha, lower_string))

unique_set = set(sorted(list(letters)))

most_common = None
qty_most_common = 0

for item in unique_set:
    qty = letters.count(item)
    if qty > qty_most_common:
        qty_most_common = qty
        most_common = item

print(most_common)
