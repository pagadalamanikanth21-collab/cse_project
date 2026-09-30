# canteen_vending_machine.py

from datetime import datetime


# =========================
# PRODUCT / INVENTORY MODULE
# =========================

products = {
    1: {"name": "Tea", "price": 15, "stock": 20},
    2: {"name": "Coffee", "price": 20, "stock": 20},
    3: {"name": "Samosa", "price": 20, "stock": 15},
    4: {"name": "Sandwich", "price": 50, "stock": 10},
    5: {"name": "Burger", "price": 60, "stock": 10},
    6: {"name": "Cold Drink", "price": 40, "stock": 15},
    7: {"name": "Water Bottle", "price": 20, "stock": 25},
    8: {"name": "Chips", "price": 30, "stock": 20}
}


# =========================
# DISPLAY MENU
# =========================

def display_menu():
    print("\n" + "=" * 60)
    print("             VIT CANTEEN VENDING MACHINE")
    print("=" * 60)

    print(f"{'ID':<5}{'ITEM':<20}{'PRICE':<12}{'STOCK':<10}")
    print("-" * 60)

    for product_id, product in products.items():
        print(
            f"{product_id:<5}"
            f"{product['name']:<20}"
            f"₹{product['price']:<11}"
            f"{product['stock']:<10}"
        )

    print("=" * 60)


# =========================
# ADD ITEM TO CART
# =========================

def add_to_cart(cart):
    try:
        product_id = int(input("Enter product ID: "))

        if product_id not in products:
            print("Invalid product ID.")
            return

        product = products[product_id]

        if product["stock"] <= 0:
            print("Sorry! This item is out of stock.")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if quantity > product["stock"]:
            print(f"Only {product['stock']} items are available.")
            return

        if product_id in cart:
            cart[product_id]["quantity"] += quantity
        else:
            cart[product_id] = {
                "name": product["name"],
                "price": product["price"],
                "quantity": quantity
            }

        print(f"{quantity} x {product['name']} added to cart.")

    except ValueError:
        print("Please enter a valid number.")


# =========================
# DISPLAY CART
# =========================

def display_cart(cart):
    if not cart:
        print("\nYour cart is empty.")
        return 0

    print("\n" + "=" * 60)
    print("                    YOUR CART")
    print("=" * 60)

    total = 0

    print(f"{'ITEM':<20}{'PRICE':<12}{'QTY':<8}{'TOTAL':<12}")
    print("-" * 60)

    for item in cart.values():
        item_total = item["price"] * item["quantity"]
        total += item_total

        print(
            f"{item['name']:<20}"
            f"₹{item['price']:<11}"
            f"{item['quantity']:<8}"
            f"₹{item_total:<11}"
        )

    print("-" * 60)
    print(f"{'TOTAL AMOUNT':<40}₹{total}")
    print("=" * 60)

    return total


# =========================
# REMOVE ITEM
# =========================

def remove_from_cart(cart):
    if not cart:
        print("Cart is empty.")
        return

    display_cart(cart)

    try:
        product_id = int(input("Enter product ID to remove: "))

        if product_id not in cart:
            print("Item is not in your cart.")
            return

        del cart[product_id]

        print("Item removed successfully.")

    except ValueError:
        print("Invalid input.")


# =========================
# PAYMENT MODULE
# =========================

def make_payment(amount):
    print("\n" + "=" * 60)
    print("                    PAYMENT")
    print("=" * 60)

    print(f"Amount to pay: ₹{amount}")

    print("\n1. Cash")
    print("2. UPI")
    print("3. Card")

    try:
        choice = int(input("Select payment method: "))

        if choice not in [1, 2, 3]:
            print("Invalid payment method.")
            return False

        if choice == 1:
            return cash_payment(amount)

        elif choice == 2:
            return upi_payment(amount)

        elif choice == 3:
            return card_payment(amount)

    except ValueError:
        print("Invalid input.")
        return False


# =========================
# CASH PAYMENT
# =========================

def cash_payment(amount):
    while True:
        try:
            cash = float(input("Enter cash amount: ₹"))

            if cash < amount:
                print(f"Insufficient amount. You need ₹{amount - cash:.2f} more.")
                continue

            change = cash - amount

            print(f"Payment successful!")
            print(f"Change returned: ₹{change:.2f}")

            return True

        except ValueError:
            print("Enter a valid amount.")


# =========================
# UPI PAYMENT
# =========================

def upi_payment(amount):
    print(f"\nUPI payment amount: ₹{amount}")

    upi_id = input("Enter UPI ID: ").strip()

    if not upi_id:
        print("Invalid UPI ID.")
        return False

    print("Processing UPI payment...")

    # Simulation
    print("UPI payment successful!")

    return True


# =========================
# CARD PAYMENT
# =========================

def card_payment(amount):
    print(f"\nCard payment amount: ₹{amount}")

    card_number = input("Enter card number: ").strip()

    if len(card_number) < 4:
        print("Invalid card number.")
        return False

    print("Processing card payment...")

    # Simulation
    print("Card payment successful!")

    return True


# =========================
# UPDATE INVENTORY
# =========================

def update_inventory(cart):
    for product_id, item in cart.items():
        products[product_id]["stock"] -= item["quantity"]


# =========================
# GENERATE RECEIPT
# =========================

def generate_receipt(cart, total):
    print("\n")
    print("=" * 60)
    print("             VIT CANTEEN - RECEIPT")
    print("=" * 60)

    print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

    print("-" * 60)

    for item in cart.values():
        item_total = item["price"] * item["quantity"]

        print(
            f"{item['name']} x {item['quantity']} "
            f"= ₹{item_total}"
        )

    print("-" * 60)

    print(f"TOTAL: ₹{total}")

    print("=" * 60)
    print("       Thank you! Visit again.")
    print("=" * 60)


# =========================
# ADMIN / STOCK MANAGEMENT
# =========================

def restock_product():
    display_menu()

    try:
        product_id = int(input("Enter product ID: "))

        if product_id not in products:
            print("Invalid product ID.")
            return

        quantity = int(input("Enter quantity to add: "))

        if quantity <= 0:
            print("Invalid quantity.")
            return

        products[product_id]["stock"] += quantity

        print(
            f"{quantity} {products[product_id]['name']}"
            " added to stock."
        )

    except ValueError:
        print("Invalid input.")


# =========================
# CUSTOMER SYSTEM
# =========================

def customer_mode():
    cart = {}

    while True:
        print("\n" + "=" * 60)
        print("                 CUSTOMER MENU")
        print("=" * 60)

        print("1. View Products")
        print("2. Add Item")
        print("3. View Cart")
        print("4. Remove Item")
        print("5. Checkout")
        print("6. Cancel Order")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            display_menu()
            add_to_cart(cart)

        elif choice == "3":
            display_cart(cart)

        elif choice == "4":
            remove_from_cart(cart)

        elif choice == "5":
            if not cart:
                print("Your cart is empty.")
                continue

            total = display_cart(cart)

            confirm = input(
                "Proceed with payment? (yes/no): "
            ).lower()

            if confirm == "yes":

                if make_payment(total):
                    update_inventory(cart)
                    generate_receipt(cart, total)
                    break

            else:
                print("Checkout cancelled.")

        elif choice == "6":
            print("Order cancelled.")
            break

        else:
            print("Invalid choice.")


# =========================
# ADMIN MODE
# =========================

def admin_mode():
    password = input("Enter admin password: ")

    if password != "admin123":
        print("Incorrect password.")
        return

    while True:
        print("\n" + "=" * 60)
        print("                   ADMIN MENU")
        print("=" * 60)

        print("1. View Inventory")
        print("2. Restock Product")
        print("3. Exit Admin Mode")

        choice = input("Enter choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            restock_product()

        elif choice == "3":
            break

        else:
            print("Invalid choice.")


# =========================
# MAIN PROGRAM
# =========================

def main():

    while True:

        print("\n" + "=" * 60)
        print("        WELCOME TO VIT CANTEEN VENDING MACHINE")
        print("=" * 60)

        print("1. Customer")
        print("2. Admin")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            customer_mode()

        elif choice == "2":
            admin_mode()

        elif choice == "3":
            print("\nThank you for using the vending machine!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program execution

if __name__ == "__main__":
    main()