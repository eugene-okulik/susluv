import datetime


class Flower:

    def __init__(self, color, length, price, date_of_cut):
        self.color = color
        self.length = length  # centimeters
        self.price = price  # russian rubles
        self.date_of_cut = datetime.datetime.strptime(date_of_cut, '%b %d %Y %H:%M')  # 'Jan 15 2023 12:05'


class Rose(Flower):
    type_of_flower = 'Rose'
    max_lifetime = 5 * 24 * 60 * 60  # seconds

    def __init__(self, color, length, price, date_of_cut):
        super().__init__(color, length, price, date_of_cut)
        self.remaining_lifetime = (
            max(0, round((Rose.max_lifetime - (datetime.datetime.now() - self.date_of_cut).total_seconds()) / 3600)))


class Tulip(Flower):
    type_of_flower = 'Tulip'
    max_lifetime = 3 * 24 * 60 * 60  # seconds

    def __init__(self, color, length, price, date_of_cut):
        super().__init__(color, length, price, date_of_cut)
        self.remaining_lifetime = (
            max(0, round((Tulip.max_lifetime - (datetime.datetime.now() - self.date_of_cut).total_seconds()) / 3600)))


class Bouquet:

    def __init__(self, *args):
        self.flowers = list(args)
        self.price = sum(map(lambda x: x.price, self.flowers))

    def freshness(self):
        return sum(map(lambda x: x.remaining_lifetime, self.flowers)) / len(self.flowers)

    def sort_by_price(self, reverse=False):
        self.flowers.sort(key=lambda x: x.price, reverse=reverse)

    def sort_by_length(self, reverse=False):
        self.flowers.sort(key=lambda x: x.length, reverse=reverse)

    def sort_by_color(self, reverse=False):
        self.flowers.sort(key=lambda x: x.color, reverse=reverse)

    def sort_by_remaining_lifetime(self, reverse=False):
        self.flowers.sort(key=lambda x: x.remaining_lifetime, reverse=reverse)

    def find_by_price(self, min=0, max=10000):
        return list(filter(lambda x: (x.price >= min) and (x.price <= max), self.flowers))

    def __str__(self):

        flowers_str =\
            "\n".join(f"  - {flower.length} cм {flower.color} {flower.type_of_flower} "
                      f"за {flower.price}" for flower in self.flowers)
        return (f"Букет из {len(self.flowers)} цветов:\n"
                f"{flowers_str}\n"
                f"Общая стоимость: {self.price} руб.\n"
                f"Средняя свежесть: {self.freshness()} часов")


rose1 = Rose('red', 35, 150, 'Aug 30 2025 19:05')
rose2 = Rose('white', 50, 300, 'Aug 29 2025 16:25')
tulip1 = Tulip('blue', 40, 250, 'Aug 29 2025 19:05')
tulip2 = Tulip('orange', 30, 200, 'Aug 30 2025 19:05')

bouquet1 = Bouquet(rose1, rose2, tulip1, tulip2)

print('=' * 10, ' Только собрали букет', '=' * 10)
print(bouquet1)
print()

print('=' * 10, ' Сортировали по цене', '=' * 10)
bouquet1.sort_by_price()
print(bouquet1)
print()

print('=' * 10, ' Обратная сортировка по цене', '=' * 10)
bouquet1.sort_by_price(reverse=True)
print(bouquet1)
print()

print('=' * 10, ' За цену от 200 до 250', '=' * 10)
filtered_by_price = bouquet1.find_by_price(min=200, max=250)
print(Bouquet(*filtered_by_price))
