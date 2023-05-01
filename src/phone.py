from src.item import Item


class Phone(Item):
    """
    Дочерний класс инициализации от класса Item.
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, " \
               f"{self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, sim_cards):
        if sim_cards > 0:
            self.__number_of_sim = sim_cards
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
