import sys
import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def print_menu():
    print("\n"
          "   Store Menu\n"
          "   ----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Place an order\n"
          "4. Quit\n")


def print_all_products(store_obj):
    all_products = store_obj.get_all_products()
    for index, product in enumerate(all_products):
        print(f"{index + 1}. {product.show()}")


def convert_to_product_index(product_number):
    try:
        chosen_product_index = int(product_number) - 1
    except ValueError:
        print("\nPlease enter a valid product number\n")
        return None
    return chosen_product_index


def get_product_index(all_products):
    while True:
        product_number = input("Which product # do you want? ")
        if product_number == '':
            return product_number
        product_index = convert_to_product_index(product_number)
        if product_index is None:
            continue
        if product_index not in range(0, len(all_products)):
            print("\nProduct number doesn't exist.\n")
            continue
        return product_index


def get_product_amount():
    while True:
        amount = input("What amount do you want? ")
        if amount == '':
            return amount
        try:
            amount = int(amount)
        except ValueError:
            print("Please enter an amount")
            continue
        return amount


def print_total_items(store_obj):
    total_quantity = store_obj.get_total_quantity()
    print(f"Total of {total_quantity} items in store.")


def place_order(store_obj):
    print("------")
    shopping_list = []
    all_products = store_obj.get_all_products()
    print_all_products(store_obj)
    print("------")
    print("\nWhenever you wish to finish placing your order, leave input empty and press enter.\n")

    while True:
        product_index = get_product_index(all_products)
        amount = get_product_amount()
        if product_index == '':
            break
        shopping_list.append((all_products[product_index], amount))
        print("Product added to list!\n")

    total = store_obj.order(shopping_list)
    print("\n********\n"
          f"\nOrder placed! Total payment: ${total}\n")

    input("Press enter to continue shopping\n")


def handle_menu_choice(user_choice, store_obj):
    if user_choice == '1':
        print_all_products(store_obj)

    elif user_choice == '2':
        print_total_items(store_obj)

    elif user_choice == '3':
        place_order(store_obj)

    elif user_choice == '4':
        sys.exit()

    else:
        print("\nInvalid choice, please try again")


def start(store_obj):
    while True:
        print_menu()
        user_choice = input("Please choose a number: ")
        handle_menu_choice(user_choice, store_obj)


start(best_buy)
