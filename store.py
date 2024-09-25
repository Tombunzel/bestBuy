class Store:
    def __init__(self, list_of_products):
        self.list_of_products = list_of_products

    def add_product(self, product):
        self.list_of_products.append(product)

    def remove_product(self, product):
        self.list_of_products.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.list_of_products:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        all_products = []
        for product in self.list_of_products:
            if product.is_active():
                all_products.append(product)
        return all_products

    def order(self, shopping_list):
        total = 0
        for product, quantity in shopping_list:
            current_total = product.buy(quantity)
            total += current_total
        return total

