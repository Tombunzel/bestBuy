import sys
import products
import promotions
import store


def setup_initial_inventory():
    """setup initial stock of inventory"""
    mac = products.Product("MacBook Air M2", price=1450, quantity=100)
    bose = products.Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    pixel = products.Product("Google Pixel 7", price=500, quantity=250)
    windows = products.NonStockedProduct("Windows License", price=125)
    shipping = products.LimitedProduct("Shipping", price=10, maximum=1, quantity=0)
    return mac, bose, pixel, windows, shipping


def setup_promotions():
    """Create promotion catalog"""
    second_half_price = promotions.SecondHalfPrice("Second Half price!")
    third_one_free = promotions.ThirdOneFree("Third One Free!")
    thirty_percent = promotions.PercentDiscount("30% off!", percentage=30)
    twenty_percent = promotions.PercentDiscount("20% off!", percentage=20)
    return second_half_price, third_one_free, thirty_percent, twenty_percent


def assign_promotions_to_products(mac, bose, pixel, windows, second_half_price,
                                  third_one_free, thirty_percent, twenty_percent):
    """assigns promotion to some products"""
    mac.promotion = second_half_price
    bose.promotion = third_one_free
    pixel.promotion = thirty_percent
    windows.promotion = twenty_percent


def print_menu():
    """prints the cli menu"""
    print("\n"
          "   Store Menu\n"
          "   ----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Place an order\n"
          "4. Quit\n")


def print_all_products(store_obj):
    """prints all products in store"""
    all_products = store_obj.get_all_products()
    for index, product in enumerate(all_products):
        print(f"{index + 1}. {product}")


def convert_to_product_index(product_number):
    """converts user input product number and returns a product index"""
    try:
        chosen_product_index = int(product_number) - 1
    except ValueError:
        print("\nPlease enter a valid product number\n")
        return None
    return chosen_product_index


def get_product_index(all_products):
    """gets a product index from the user"""
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
    """gets a product amount to be bought"""
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
    """print total quantity of items in the store"""
    total_quantity = store_obj.get_total_stock()
    print(f"Total of {total_quantity} items in store.")


def place_order(store_obj):
    """allows the user to place an order by item number and chosen quantity,
    finally showing the total amount to pay"""
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
        print("Product(s) added to list!\n")

    while True:
        total = store_obj.order(shopping_list)
        print("\n********")
        if total == 0 or (len(shopping_list) == 1 and shopping_list[0][0].name == 'Shipping'):
            print("\nShopping list empty, order was not placed.\n")
            break
        print(f"\nOrder placed! Total payment: ${total}\n")
        break

    input("Press enter to continue shopping\n")


def handle_menu_choice(user_choice, store_obj):
    """handles the user's choice from the menu"""
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
    """prints the cli menu, gets user choice and handles it
    until the user chooses to exit the program"""
    while True:
        print_menu()
        user_choice = input("Please choose a number: ")
        handle_menu_choice(user_choice, store_obj)


def main():
    """sets up initial inventory and promotions, assigns latter to former,
    instantiates a store object and starts the store app"""
    mac, bose, pixel, windows, shipping = setup_initial_inventory()
    second_half_price, third_one_free, thirty_percent, twenty_percent = setup_promotions()
    assign_promotions_to_products(mac, bose, pixel, windows, second_half_price,
                                  third_one_free, thirty_percent, twenty_percent)
    best_buy = store.Store([mac, bose, pixel, windows, shipping])
    start(best_buy)


if __name__ == "__main__":
    main()
