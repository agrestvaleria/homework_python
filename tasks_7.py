# 1. Создайте класс book с именем книги, автором, кол-м страниц, ISBN, флагом,
# зарезервирована ли книги или нет. Создайте класс пользователь который может брать книгу, возвращать, бронировать.
# Если другой пользователь хочет взять зарезервированную книгу(или которую уже кто-то читает - надо ему про это сказать).

store_isbn = []


def take_reserve(option, store, isbn):
    res = ''
    if len(store) == 0:
        option += 1
        store.append(isbn)
        res += 'You have'
    else:
        if isbn in store:
            res += 'should have a different ISBN, this one is used'
        else:
            option += 1
            store.append(isbn)
            res += 'You have'
    return res


class Book:

    def __init__(self, book, author, pages, isbn, reserved, taken):
        self.book = book
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = reserved
        self.taken = taken


class User:

    def __init__(self):
        self.books = []

    def book_to_take(self, a_book):
        self.books.append(a_book)

    def take_book(self):
        for a_book in self.books:
            if a_book.taken == 0 and a_book.reserved != 0:
                print(f'{a_book.book} has already reserved. '
                      f'Please choose another book to take.')
            elif a_book.taken != 0:
                print(f'{a_book.book} has already taken. '
                      f'Please choose another book to take.')
            else:
                result = take_reserve(a_book.taken, store_isbn, a_book.isbn)
                if result == 'You have':
                    print(f'{result} taken {a_book.book}')
                else:
                    print(f"{a_book.book} {result}")

    def reserve_book(self):
        for a_book in self.books:
            if a_book.taken == 0 and a_book.reserved == 0:
                print(f'You have reserved {a_book.book}.')
                a_book.reserved += 1
            elif a_book.taken != 0 and a_book.reserved == 0:
                print(f'{a_book.book} has already taken. '
                      f'Please choose another book to reserve.')
            elif a_book.reserved != 0:
                print(f'{a_book.book} has already reserved. '
                      f'Please choose another book to reserve.')
            else:
                result = take_reserve(a_book.reserved, store_isbn, a_book.isbn)
                if result == 'You have':
                    print(f'{result} reserved {a_book.book}')
                else:
                    print(f"{a_book.book} {result}")

    def bring_back_book(self):
        for a_book in self.books:
            if a_book.taken == 1:
                a_book.taken = 0
                store_isbn.remove(a_book.isbn)
                print(f'Thank you for bringing back {a_book.book}')


book = Book('A Walk to Remember', 'Nicholas Sparks', 240, 'ISBN_1', 0, 0)
book2 = Book('The Stand', 'Stephen King', 300, 'ISBN_1', 0, 0)
book3 = Book('The Thorn Birds', 'Colleen McCullough', 310, 'ISBN_2', 0, 0)
User1 = User()
User1.book_to_take(book)
User1.take_book()
User2 = User()
User2.book_to_take(book2)
User2.take_book()
User3 = User()
User3.book_to_take(book3)
User3.take_book()

# 2. Создайте класс инвестиция.
# Который содержит необходимые поля и методы, например сумма инвестиция и его срок.
# Пользователь делает инвестиция в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму, которая будет на счету пользователя.


class Investment:

    def __init__(self, summa, period, percent):
        self.summa = summa
        self.period = period
        self.percent = percent


class Bank:

    def __init__(self):
        self.invests = list()

    def add_invest(self, invest):
        self.invests.append(invest)

    def deposit(self):
        for invest in self.invests:
            period_in_months = invest.period * 12
            one_month = invest.percent / 12
            for i in range(1, period_in_months + 1):
                new_summa = invest.summa + (invest.summa * one_month) / 100
                invest.summa = round(new_summa, 2)
            print(f'Summa will be {invest.summa}')


investment = Investment(2000, 1, 10)
bank = Bank()
bank.add_invest(investment)
bank.deposit()
