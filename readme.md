VIT Canteen Vending Machine

A console-based Python vending machine application designed to simulate a canteen ordering system. The application allows customers to browse products, add items to a cart, make payments, and receive a receipt. It also provides an admin mode for viewing and restocking inventory.

Features
Customer Features

View available food and beverage products.

View product prices and current stock.

Add products to a shopping cart.

Specify the required quantity.

View cart contents and total amount.

Remove items from the cart.

Checkout and make payment.

Support for multiple payment methods:

Cash

UPI

Card

Automatic inventory update after successful payment.

Generate a receipt containing:

Purchased items

Quantities

Total amount

Date and time

Admin Features

Secure admin login using a password.

View current inventory.

Restock existing products.

Automatically update stock quantities.

Technologies Used

Python 3

Python datetime module

Console/terminal interface

Dictionaries for product and cart management

Functions for modular program design

Project Structure
canteen_vending_machine.py
README.md


The complete application is implemented in:

canteen_vending_machine.py

Product Inventory

The application initially contains the following products:

ID	Product	Price	Initial Stock
1	Tea	₹15	20
2	Coffee	₹20	20
3	Samosa	₹20	15
4	Sandwich	₹50	10
5	Burger	₹60	10
6	Cold Drink	₹40	15
7	Water Bottle	₹20	25
8	Chips	₹30	20
Requirements

Make sure Python 3.x is installed on your computer.

Check your Python installation using:

python --version


or:

python3 --version


No external Python packages are required.

How to Run
1. Clone or download the project

Download the project files to your computer.

2. Open the project directory

Navigate to the directory containing:

canteen_vending_machine.py

3. Run the program

On Windows:

python canteen_vending_machine.py


On Linux/macOS:

python3 canteen_vending_machine.py

Main Menu

When the program starts, the following menu is displayed:

============================================================
        WELCOME TO VIT CANTEEN VENDING MACHINE
============================================================
1. Customer
2. Admin
3. Exit
Enter your choice:

Customer Mode

Select:

1. Customer


The customer menu provides:

============================================================
                 CUSTOMER MENU
============================================================
1. View Products
2. Add Item
3. View Cart
4. Remove Item
5. Checkout
6. Cancel Order

Example Customer Workflow

Select Customer.

View available products.

Select Add Item.

Enter the product ID.

Enter the desired quantity.

View the cart.

Remove items if required.

Select Checkout.

Confirm payment.

Select a payment method.

Complete the simulated payment.

Receive the generated receipt.

Payment Methods

The program supports three payment options.

Cash

The customer enters the cash amount.

If the amount is greater than the bill:

Payment successful!
Change returned: ₹20.00


If the amount is insufficient, the program asks the customer to enter another amount.

UPI

The customer enters a UPI ID.

The current implementation simulates successful UPI payment and does not connect to an actual payment gateway.

Card

The customer enters a card number.

The program performs basic validation and simulates a successful card payment. No real card transaction is performed.

Important: This project is an educational simulation. It does not process real payments.

Admin Mode

Select:

2. Admin


The application asks for an admin password.

Default Admin Password
admin123


After successful authentication, the admin menu appears:

============================================================
                   ADMIN MENU
============================================================
1. View Inventory
2. Restock Product
3. Exit Admin Mode

Restocking

The admin can select a product and enter the quantity to add.

For example:

Enter product ID: 4
Enter quantity to add: 10


The sandwich stock will increase by 10.

Receipt

After successful checkout, the program generates a receipt similar to:

============================================================
             VIT CANTEEN - RECEIPT
============================================================
Date: 28-09-2026 10:30:45
------------------------------------------------------------
Tea x 2 = ₹30
Samosa x 1 = ₹20
------------------------------------------------------------
TOTAL: ₹50
============================================================
       Thank you! Visit again.
============================================================

Program Modules

The program is divided into several functional modules.

1. Product / Inventory Module

Stores all available products and their:

Product ID

Name

Price

Stock quantity

products = {
    1: {"name": "Tea", "price": 15, "stock": 20},
    ...
}

2. Display Menu

The display_menu() function displays all available products, prices, and stock.

3. Shopping Cart

The add_to_cart() function allows customers to add products to their cart.

The display_cart() function calculates and displays the total bill.

4. Remove Item

The remove_from_cart() function allows customers to remove products from their cart.

5. Payment Module

The make_payment() function provides the payment selection menu.

Payment functions include:

cash_payment()
upi_payment()
card_payment()

6. Inventory Update

The update_inventory() function reduces product stock after a successful purchase.

7. Receipt Generation

The generate_receipt() function creates a transaction receipt containing the purchased items, total amount, and date/time.

8. Admin / Stock Management

The restock_product() function allows administrators to add stock to existing products.

9. Customer System

The customer_mode() function manages the complete customer workflow.

10. Admin System

The admin_mode() function handles administrator authentication and inventory management.

11. Main Program

The main() function displays the application's main menu and controls navigation between customer and admin modes.

Program Flow
                  START
                    |
                    v
             Display Main Menu
                    |
          +---------+---------+
          |         |         |
          v         v         v
      Customer    Admin      Exit
          |         |         |
          v         v         v
     Customer    Password   End Program
       Menu        |
          |        v
          |    Admin Menu
          |        |
          |    View/Restock
          |
          v
     View Products
          |
          v
       Add Items
          |
          v
       View Cart
          |
          v
     Remove Items
          |
          v
       Checkout
          |
          v
      Payment
          |
     +----+----+
     |    |    |
   Cash  UPI  Card
     |    |    |
     +----+----+
          |
          v
    Payment Successful
          |
          v
   Update Inventory
          |
          v
    Generate Receipt
          |
          v
          END

Data Structures
Products Dictionary

Products are stored using a Python dictionary:

products = {
    1: {
        "name": "Tea",
        "price": 15,
        "stock": 20
    }
}


The product ID is used as the dictionary key.

Cart Dictionary

The customer's cart is also represented using a dictionary:

cart = {
    1: {
        "name": "Tea",
        "price": 15,
        "quantity": 2
    }
}


This makes it easy to calculate totals and update quantities.

Input Validation

The program includes basic validation for:

Invalid product IDs

Invalid quantities

Zero or negative quantities

Insufficient stock

Invalid payment methods

Invalid cash amounts

Empty UPI IDs

Invalid card numbers

Incorrect admin password

Non-numeric input where numbers are expected

Important Notes

This application is intended primarily as an academic/project demonstration.

The following features are simulated:

UPI payments

Card payments

Authentication security

Transaction processing

No actual payment gateway or banking service is connected.

The inventory is stored only in program memory. Therefore, stock changes are lost when the application is closed.

Limitations

Current limitations include:

Inventory is not stored permanently.

Orders are not saved to a database or file.

UPI payments are simulated.

Card payments are simulated.

The admin password is hard-coded.

There is no user account system.

There is no transaction history.

There is no graphical user interface.

There is no tax/GST calculation.

There is no discount or coupon system.

Possible Future Improvements

The project can be extended with:

SQLite/MySQL database integration.

Persistent inventory storage.

Customer registration and login.

Secure password hashing.

Order history.

Transaction IDs.

GST/tax calculation.

Discounts and coupons.

Multiple vending machines.

Low-stock alerts.

Sales reports for administrators.

Real payment gateway integration.

QR-code-based UPI payments.

Graphical user interface using Tkinter.

Web-based interface using Flask or Django.

Improved cart quantity management.

Automated unit and integration testing.

Example Use Case

A customer wants to purchase:

2 × Tea = ₹30

1 × Samosa = ₹20

1 × Chips = ₹30

The total bill is:

₹30 + ₹20 + ₹30 = ₹80


The customer selects a payment method and completes the simulated payment.

After successful payment:

The stock of Tea decreases by 2.

The stock of Samosa decreases by 1.

The stock of Chips decreases by 1.

A receipt is generated.

The customer order is completed.

Error Handling

The application uses try-except blocks to handle invalid numeric input.

For example:

try:
    quantity = int(input("Enter quantity: "))
except ValueError:
    print("Please enter a valid number.")


This prevents the program from terminating when the user enters invalid numeric data.

Security Notice

The default admin password is:

admin123


This password is hard-coded for demonstration purposes and should not be used in a production application.

Similarly, the application should never collect or store real card numbers or payment credentials without appropriate security and compliance measures.

Author

VIT Canteen Vending Machine Project

Developed as a Python programming project demonstrating:

Functions

Dictionaries

Conditional statements

Loops

Exception handling

Input validation

Modular programming

Basic inventory management

Payment simulation

License

This project is intended for educational and academic use.