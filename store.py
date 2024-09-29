class Store:
    """class Store for handling purchases and quantities etc."""

    def __init__(self, products):
        """constructor"""
        self._products = products

    @property
    def products(self):
        return self._products

    @products.setter
    def products(self, new_products):
        self._products = new_products

    def add_product(self, product):
        """adds a product to list of products"""
        self._products.append(product)

    def remove_product(self, product):
        """removes product from list of products"""
        self._products.remove(product)

    def get_total_stock(self):
        """returns the total amount of items in store"""
        total_stock = 0
        for product in self._products:
            total_stock += product.quantity
        return total_stock

    def get_all_products(self):
        """returns a list of all active products in store"""
        all_products = []
        for product in self._products:
            if product.is_active():
                all_products.append(product)
        return all_products

    @staticmethod
    def order(shopping_list):
        """returns total price of order"""
        total = 0
        for product, quantity in shopping_list:
            current_total = product.buy(quantity)
            total += current_total
        return total

    def __contains__(self, item):
        return item in self.products
