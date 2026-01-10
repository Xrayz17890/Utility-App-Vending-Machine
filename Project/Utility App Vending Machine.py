vending_items = {
    "D1": {"name": "Coffee", "price": 5.0, "stock": 5, "category": "Drinks"},
    "D2": {"name": "Tea", "price": 4.0, "stock": 5, "category": "Drinks"},
    "D3": {"name": "Water", "price": 2.0, "stock": 10, "category": "Drinks"},
    "S1": {"name": "Chocolate Bar", "price": 3.5, "stock": 6, "category": "Snacks"},
    "S2": {"name": "Biscuits", "price": 3.0, "stock": 6, "category": "Snacks"},
}


def display_menu():
    """Displays available items grouped by category"""
    print("\n====== VENDING MACHINE MENU ======")
    categories = set(item["category"] for item in vending_items.values())

    for category in categories:
        print(f"\n-- {category} --")
        for code, item in vending_items.items():
            if item["category"] == category:
                print(f"{code}: {item['name']} - {item['price']} SAR (Stock: {item['stock']})")


def get_item(code):
    """Returns item if valid, otherwise None"""
    return vending_items.get(code)


def process_payment(price):
    """Handles payment and returns change"""
    while True:
        try:
            money = float(input(f"Insert money (SAR {price} required): "))
            if money < price:
                print("Not enough money. Please insert more.")
            else:
                return round(money - price, 2)
        except ValueError:
            print("Invalid input. Please enter a number.")


def suggest_item(selected_item):
    """Suggests an item based on previous purchase"""
    if selected_item["name"] == "Coffee":
        print("Suggestion: Would you like to add Biscuits (S2)?")


def vending_machine():
    """Main vending machine logic"""
    print("Welcome to the Vending Machine!")

    while True:
        display_menu()
        choice = input("\nEnter item code (or Q to quit): ").upper()

        if choice == "Q":
            print("Thank you for using the Vending Machine. Goodbye!")
            break

        item = get_item(choice)
        if not item:
            print("Invalid code. Please try again.")
            continue

        if item["stock"] <= 0:
            print("Sorry, this item is out of stock.")
            continue

        print(f"You selected {item['name']} - {item['price']} SAR")
        change = process_payment(item["price"])

        item["stock"] -= 1
        print(f"{item['name']} has been dispensed.")
        print(f"Your change is: {change} SAR")

        suggest_item(item)

        another = input("\nWould you like to buy another item? (Y/N): ").upper()
        if another != "Y":
            print("Thank you for your purchase. Have a great day!")
            break


def main():
    vending_machine()


if __name__ == "__main__":
    main()
