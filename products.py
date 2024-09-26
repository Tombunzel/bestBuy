class Product:
    """class Product for activating, showing and handling products"""

    def check_init(self):
        if not self.name:
            raise ValueError("Product name can't be empty")
        if self.price < 0:
            raise ValueError("Product price can't be lower than 0")
        if self.quantity < 0:
            raise ValueError("Product quantity can't be lower than 0")

    def __init__(self, name, price, quantity):
        """constructor"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.check_init()

    def get_quantity(self):
        """returns quantity of a product"""
        return self.quantity

    def set_quantity(self, quantity):
        """set quantity of a product"""
        if quantity == 0:
            self.active = False
        self.quantity = quantity

    def is_active(self):
        """returns whether a product is active"""
        return self.active

    def activate(self):
        """activates a product"""
        self.active = True

    def deactivate(self):
        """deactivates a product"""
        self.active = False

    def show(self):
        """returns a string of item name, price and available quantity"""
        return f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """returns the price to pay for a product in given quantity"""
        if self.quantity >= quantity or self.quantity == 0:
            self.quantity -= quantity
            if self.quantity == 0:
                self.deactivate()
            return self.price * quantity
        raise ValueError("Unable to buy quantity larger than in stock")


class NonStockedProduct(Product):
    def __init__(self, name, price):
        super().__init__(name, price, quantity=0)
        self.name = name
        self.price = price
        self.quantity = 0

    def show(self):
        return f"{self.name}, Price: ${self.price}, Quantity: Unlimited"


class LimitedProduct(Product):
    def __init__(self, name, price, quantity, maximum):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def show(self):
        return (f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}, "
                f"Maximum quantity per order: {self.maximum}")
