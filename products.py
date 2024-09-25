class Product:
    """class Product for activating, showing and handling products"""
    def __init__(self, name, price, quantity):
        """constructor"""
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

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
        if self.quantity >= quantity:
            self.quantity -= quantity
            return self.price * quantity
        print("\nCouldn't complete purchase, not enough items in stock.\n")
        return None
