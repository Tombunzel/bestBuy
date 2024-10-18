from abc import ABC, abstractmethod


class Promotion(ABC):
    """promotion class"""
    def __init__(self, name):
        """initializer"""
        self._name = name

    @property
    def name(self):
        """getter for name"""
        return self._name

    @name.setter
    def name(self, new_name):
        """setter for name"""
        self._name = new_name

    @abstractmethod
    def apply_promotion(self, product, quantity):
        """abstract method, implemented in child classes"""
        pass


class SecondHalfPrice(Promotion):
    """class of half-price on second item promotion"""
    def __init__(self, name):
        """initializer inheriting from super class"""
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """apply half-price on second item(s)"""
        half_priced_products = quantity // 2
        return (product.price * quantity) - ((product.price / 2) * half_priced_products)


class ThirdOneFree(Promotion):
    """class for third item free promotion"""
    def __init__(self, name):
        """initializer inheriting from super class"""
        super().__init__(name)

    def apply_promotion(self, product, quantity):
        """
        count the number of 'third items',
        then remove that number from the final price calc
        """
        free_products = quantity // 3
        return product.price * (quantity - free_products)


class PercentDiscount(Promotion):
    """class for percentage discount"""
    def __init__(self, name, percentage):
        """initializer inheriting from super class
        and percentage in addition
        """
        super().__init__(name)
        self._percentage = percentage

    def apply_promotion(self, product, quantity):
        """apply percentage discount"""
        return product.price * quantity * (1 - self._percentage / 100)
