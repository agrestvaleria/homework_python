# Цветочница.
# Определить иерархию и создать несколько цветов. Собрать букет (можно использовать аксессуары) с определением его стоимости.
# Определить время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость...)
# Реализовать поиск цветов в букете по определенным параметрам.
# Узнать, есть ли цветок в букете.

import operator


class Flower:

    def __init__(self, name, life_time=8, color='white',
                 fresh=True, length=7, price=5):
        self.life_time = life_time
        self.color = color
        self.fresh = fresh
        self.length = length
        self.price = price
        self.name = name


class RedRose(Flower):
    pass


class Marigold(Flower):
    pass


class Tulip(Flower):
    pass


class CollectBouquet:

    def __init__(self, fl, counts):
        self.fl = fl
        self.counts = counts

    def price_of_bouquet(self):
        price_list = []
        for flower in self.fl:
            each_price = self.counts[self.fl.index(flower)] * flower.price
            price_list.append(each_price)
        print(f"The price of the bouquet is {sum(price_list)}")

    def withering_time(self):
        lifetime = []
        for flower in self.fl:
            lifetime.append(flower.life_time)
        lifetime = round(sum(lifetime) / len(self.fl), 1)
        print(f"The withering time of the bouquet is {lifetime} days")

    def sort_option(self, option):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        option_dict = {}
        for el in self.fl:
            option_dict[el.name] = operator.attrgetter(option)(el)
        sorted_dict = sorted(option_dict.items(), key=lambda fl: fl[1])
        for element in sorted_dict:
            print(element[0], element[1])

    def search_option(self, option, value):
        assert isinstance(option, str), "Option should be str"
        assert len(option), "Please enter an option"
        assert option in ['life_time', 'price', 'length', 'color', 'fresh'], \
            f"There is no such option {option}"
        assert isinstance(value, int), "Value should be int"
        assert value > 0, "Value must be positive"
        flower_list = []
        for el in self.fl:
            if operator.attrgetter(option)(el) == value:
                flower_list.append(el.name)
        if len(flower_list) > 0:
            name_list_search = ", ".join(flower_list)
            print(name_list_search)
        else:
            print('There is no such flower in the bouquet')

    def search_flower(self, el):
        assert isinstance(el, str), "The name of a flower should be str"
        assert len(el), "Please enter the name of a flower"
        if el in [flower.name for flower in self.fl]:
            print(f"{el} is in the bouquet")
        else:
            print(f"{el} is not in the bouquet")


red_rose = RedRose(name='Red Rose', life_time=3, color='red', price=30)
tulip = Tulip(name='Tulip', color='orange', fresh=False, length=5)
marigold = Marigold(name='Marigold', life_time=4, color='yellow', length=4)
flowers = [red_rose, tulip, marigold]
counts = [2, 3, 4]
collect_bouquet = CollectBouquet(flowers, counts)
collect_bouquet.price_of_bouquet()
collect_bouquet.withering_time()
collect_bouquet.sort_option('color')
collect_bouquet.search_option('length', 4)
collect_bouquet.search_flower('Tulip')
