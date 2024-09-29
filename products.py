from abc import ABC


class Product(ABC):
    """class Product for activating, showing and handling products"""

    def __init__(self, name, price, quantity, promotion=None):
        """constructor"""
        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion = promotion
        self.check_init()

    def check_init(self):
        if not self._name:
            raise ValueError("Name cannot be empty!")
        if self._price < 0:
            raise ValueError("Price cannot be less than 0!")
        if self._quantity < 0:
            raise ValueError("Product quantity cannot be less than 0!")

    @property
    def name(self):
        if not self._name:
            raise ValueError("Product name can't be empty")
        return self._name

    @name.setter
    def name(self, new_name):
        if not new_name:
            raise ValueError("Product name can't be empty")
        self._name = new_name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price < 0:
            raise ValueError("Product price can't be lower than 0")
        self._price = new_price

    @property
    def promotion(self):
        return self._promotion

    @promotion.setter
    def promotion(self, new_promotion):
        self._promotion = new_promotion

    @property
    def quantity(self):
        """returns quantity of a product"""
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """set quantity of a product"""
        if quantity < 0:
            raise ValueError("Product quantity can't be lower than 0")
        if quantity == 0:
            self._active = False
        self._quantity = quantity

    def is_active(self):
        """returns whether a product is active"""
        return self._active

    def activate(self):
        """activates a product"""
        self._active = True

    def deactivate(self):
        """deactivates a product"""
        self._active = False

    def __str__(self):
        """returns a string of item name, price and available quantity"""
        if self.quantity == 0:
            product_string = f"{self._name}, Price: ${self._price}, Quantity: Unlimited"
        else:
            product_string = f"{self._name}, Price: ${self._price}, Quantity: {self._quantity}"
        if self.promotion:
            return f"{product_string}, Promotion: {self.promotion.name}"
        return product_string

    def buy(self, quantity):
        """returns the price to pay for a product in given quantity"""
        if isinstance(self, LimitedProduct) and quantity != 1:
            print(f"\nAutomatically corrected {self._name} amount from '{quantity}' to {self._maximum}.")
            return self._price * self._maximum

        if self._quantity >= quantity:
            self._quantity -= quantity
            if self._quantity == 0:
                self.deactivate()
            if self._promotion:
                return self.promotion.apply_promotion(self, quantity)
            return self._price * quantity

        if self.quantity == 0:
            if self._promotion:
                return self.promotion.apply_promotion(self, quantity)
            return self._price * quantity

        raise ValueError("Unable to buy quantity larger than in stock")

    def __gt__(self, other):
        return self.price > other.price


class NonStockedProduct(Product, ABC):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self._name = name
        self._price = price
        self._quantity = 0


class LimitedProduct(Product, ABC):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self._maximum = maximum

    def __str__(self):
        product_string = f'{self._name}, Price: ${self._price}'

        if self._quantity > 0:
            product_string += f', Quantity: {self._quantity}'

        product_string += f', Limited to {self._maximum} per order!'

        return product_string
