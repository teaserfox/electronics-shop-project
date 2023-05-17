import csv
import os


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
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Item.all.append(self)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f"{self.__name}"

    @property
    def name(self) -> str:
        """
        Геттер для названия товара
        """
        return self.__name

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item и дочерние от них.')
        return self.quantity + other.quantity

    @name.setter
    def name(self, name):
        if len(name) < 10:
            self.__name = name
        else:
            raise ValueError('Длина наименования товара превышает 10 символов')

    @classmethod
    def instantiate_from_csv(cls, CSV_FILE=os.path.join('..', 'src', 'items.csv')):
        try:
            with open(CSV_FILE, encoding='windows-1251', newline='') as file:
                reader = csv.DictReader(file)
                if len(list(csv.reader(file))[0]) != 3:
                    raise InstantiateCSVError(f'Файл {CSV_FILE} поврежден')
                file.seek(0)
                for row in reader:
                    cls.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {CSV_FILE}')
        except PermissionError:
            print(f'Невозможно создать файл {CSV_FILE}')

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Преобразование строки в число.
        """
        return int(float(number))

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


class InstantiateCSVError(Exception):
    pass
