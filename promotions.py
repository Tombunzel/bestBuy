from abc import ABC, abstractmethod


class Promotion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        pass


class SecondHalfPrice(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        half_priced_products = quantity // 2
        return (product.price * quantity) - ((product.price / 2) * half_priced_products)


class ThirdOneFree(Promotion):
    def __init__(self, name):
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        free_products = quantity // 3
        return product.price * (quantity - free_products)


class PercentDiscount(Promotion):
    def __init__(self, name, percentage):
        super().__init__(name)
        self.percentage = percentage

    def apply_promotion(self, product, quantity):
        return product.price * quantity * (1 - self.percentage / 100)
