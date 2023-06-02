class Resto:

    def __init__(self, menu: dict):
        self.menu = menu
        self.orders = {key: 0 for (key, value) in menu.items()}

    def display_menu(self):
        print("{:>25} : Price".format("Item Name"))
        for item in self.menu:
            print(f"{item:>25} : ${self.menu[item]}")
        print()
    
    def add_order(self, item: str, qty: int):
        self.orders[item] += qty
    
    def display_orders(self):
        total = 0
        for item, qty in self.orders.items():
            price = self.menu[item]
            print("{} {} for ${} each -> {}".format(qty, item, price, qty * price))
            total += qty * price
        print(f"Your total is: ${total}")

if __name__ == "__main__":
    menu = {
        "Pork and Chive Dumplings" : 10,
        "Chicken Dumplings" : 12,
        "Shrimp Dumplings" : 15,
        "Fried Rice" : 14,
        "Truffle Noodles" : 40,
    }
    dumpling_hut = Resto(menu)

    print("Please request for items in the following format: 'qty, item_name'. Write 'stop' to end meal.\n")
    dumpling_hut.display_menu()
    while(True):
        order = input('Next Order: ')
        if order.lower() == "stop":
            print()
            dumpling_hut.display_orders()
            break

        order_ls = order.split(', ')
        try:
            item = order_ls[1]
            qty = int(order_ls[0])
        except (IndexError, ValueError):
            print("Please enter items in a valid format: 'qty, item_name'.")
            continue

        if item not in dumpling_hut.menu:
            print("Please input a valid menu item.")
        else:
            dumpling_hut.add_order(item, qty)
