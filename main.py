import os
from random import Random

cls = lambda: os.system('cls')


class Product:

    def __init__(self, name, descriptions):
        self.name = name
        self.descriptions = descriptions
        self.price = Random().randint(1000, 10000)

    def __str__(self):
        return f'{self.name} цена: {self.price}'


class Store:

    def __init__(self):
        self.products = {1: Product('TestProduct 1', 'TestDescriptions 1')}

    def show_products(self):
        [print(f'{product_id} {product}', end='\n') for product_id, product in self.products.items()]

    def get_product(self, product_id):
        return self.products[product_id]

    def add_product(self, name, descriptions):
        product_id = max(self.products.keys()) + 1
        self.products[product_id] = Product(name, descriptions)

    def delete_product(self, product_id):
        self.products.pop(product_id)


class Basket:

    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def delate_product(self, product):
        self.products.remove(product)

    def show_products(self):
        print('Корзина:')
        [print(product, end='\n') for product in self.products]


class Order:

    def __init__(self):
        self.number = Random().randint(1000, 10000)
        self.address = 'default'
        self.status = 'Ожидает отправки'

    def __str__(self):
        return f'{self.status} {self.address}'


class Seller:

    def __init__(self):
        self.orders = {}

    def add_order(self, order):
        self.orders[order.number] = order

    def get_report(self):
        [print(f'{order_id} {order}', end='\n') for order_id, order in self.orders.items()]

    def send_order(self, order_id):
        if not self.orders.get(order_id, None):
            return False
        self.orders[order_id].status = 'Отправлен'
        return True


def menu(status):
    cls()
    if status:
        cls()
        print('1 - Посмотреть товары')
        print('2 - Добавить товар в корзину')
        print('3 - Удалить товар из корзины')
        print('4 - Показать товары в корзине')
        print('5 - Оформить заказ')
    else:
        cls()
        print('6 - Посмотреть заказы')
        print('7 - Выдать заказ')
        print('8 - Добавить товар')
        print('9 - Удалить товар')

    print('0 - Смена пользователя')
    print('Введите любой символ для выхода')
    key = input('Введите номер функции:')
    cls()
    return key


def main():
    store = Store()
    basket = Basket()
    seller = Seller()
    menu_status = -1

    while 1:
        if menu_status == -1:
            menu_status = int(input('Выберите пользователя:\n 1 - Покупатель \n 0 - Продавец\n'))
            cls()
        match menu(menu_status):
            case '1':
                store.show_products()
                input('Введите...')
            case '2':
                product_id = int(input('Введите номер товара'))
                basket.add_product(store.get_product(product_id))
            case '3':
                product_id = int(input('Введите номер товара'))
                basket.delate_product(store.get_product(product_id))
            case '4':
                basket.show_products()
                input('Введите...')
            case '5':
                order = Order()
                seller.add_order(order)
                print(f'Заказ с номером #{order.number} по адресу {order.address} ожидает отправки')
                input('Введите...')
            case '6':
                print('Номер Статус Адрес')
                seller.get_report()
                input('Введите...')
            case '7':
                if not seller.send_order(int(input('Введите номер заказа'))):
                    input('Заказ с таким номером не найден')
            case '8':
                name, descriptions = input('Введите название и описание через пробел').split(' ')
                store.add_product(name, descriptions)
                input('Введите...')
            case '9':
                store.delete_product(int(input('Введите номер товара')))
            case '0':
                menu_status = -1
            case _:
                break


if __name__ == '__main__':
    main()
