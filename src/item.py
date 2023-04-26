import os
import csv

PATH = os.path.csv('items.csv')


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """ Возвращает наименование товара
        """
        return f'{self.__name}'

    @name.setter
    def name(self, name) -> None:
        """ Метод срабатывает при операции присваивания. Измеряется длинна ввода символов названия.
        """
        self.__name = name
        if len(self.__name) >= 10:
            print("Длина наименования товара превышает 10 символов.")
        else:
            print("Длина наименования товара меньше 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        item_list = []
        with open('path', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                item_list.append(Item(name, price, quantity))
            cls.all = item_list

    def string_to_number(self):
        pass
