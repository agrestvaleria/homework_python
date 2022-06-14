# 1.Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'

a = 'www.my_site.com#about'
print(a.replace('#', '/'))


# 2.Напишите программу, которая добавляет ‘ing’ к словам
def programme_ing(s):
    custom_string = ''
    for word in s.split():
        custom_string += word + 'ing '

    print(custom_string)


programme_ing('say hello everyone')


# 3.В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"

d = 'Ivanou Ivan'


def rev2(s):
    words = s.split(' ')
    reverse_str = ' '.join(reversed(words))
    print(reverse_str)


rev2(d)


# 4.Напишите программу которая удаляет пробел в начале, в конце строки

def delete_space(s):
    print(s.strip())


delete_space('   I am here ')
delete_space('  Скоро Новый год     ')
