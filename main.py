import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("\n"
              "   Store Menu\n"
              "   ----------\n"
              "1. List all products in store\n"
              "2. Show total amount in store\n"
              "3. Make an order\n"
              "4. Quit\n")
        user_choice = input("Please choose a number: ")
        if user_choice == '1':
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.show())
        elif user_choice == '2':
            total_quantity = store_obj.get_total_quantity()
            print(f"Total of {total_quantity} items in store.")
        elif user_choice == '3':
            shopping_list = []
            print("------")
            all_products = store_obj.get_all_products()
            for index, product in enumerate(all_products):
                print(f"{index + 1}. {product.show()}")
            print("------")

            print("\nWhenever you wish to finish placing your order, leave input empty and press enter.\n")
            while True:
                chosen_product_number = input("Which product # do you want? ")
                if not chosen_product_number:
                    break

                try:
                    chosen_product_index = int(chosen_product_number) - 1
                except ValueError:
                    print("\nPlease enter a valid product number\n")
                    continue

                if chosen_product_index not in range(0, len(all_products)):
                    print("\nProduct number doesn't exist.\n")
                    continue

                try:
                    amount = int(input("What amount do you want? "))
                except ValueError:
                    print("Please enter an amount")
                    continue

                try:
                    shopping_list.append((all_products[chosen_product_index], amount))
                    print("Product added to list!\n")
                except IndexError:
                    print("\nProduct number doesn't exist, please try again\n")
                    continue

            total = store_obj.order(shopping_list)
            print("\n********\n"
                  f"\nOrder placed! Total payment: ${total}\n")

            input("Press enter to continue shopping\n")
        elif user_choice == '4':
            quit()
        else:
            print("\nInvalid choice, please try again")


start(best_buy)
