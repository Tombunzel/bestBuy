class Store:
    """class Store for handling purchases and quantities etc."""
    def __init__(self, list_of_products):
        """constructor"""
        self.list_of_products = list_of_products

    def add_product(self, product):
        """adds a product to list of products"""
        self.list_of_products.append(product)

    def remove_product(self, product):
        """removes product from list of products"""
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        """returns the total amount of items in store"""
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """returns a list of all active products in store"""
        all_products = []
        for product in self.list_of_products:
            if product.is_active():
                all_products.append(product)
        return all_products


def order(shopping_list):
    """returns total price of order"""
    total = 0
    for product, quantity in shopping_list:
        current_total = product.buy(quantity)
        if current_total is None:
            return None
        total += current_total
    return total
