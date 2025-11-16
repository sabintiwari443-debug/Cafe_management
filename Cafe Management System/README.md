# Py Cafe – Python Billing System

This project is a simple **food ordering and billing system** written in Python. It allows users to order items from a predefined menu, select quantities, view unavailable item messages, and get the final bill.

---

##  Features

* Displays a menu with item names and prices
* Allows users to order multiple items
* Asks for quantity of each item
* Calculates total bill based on price × quantity
* Handles unavailable items gracefully
* Loops until the customer says the order is complete

---

##  How It Works

1. The program shows a welcome message and the available menu.
2. The user types the name of the item they want to order.
3. If the item exists, the user is asked to enter the quantity.
4. The cost is added to the total bill.
5. The program asks if the user wants to order more items.
6. When finished, the final bill is displayed.

---

##  Code Used

```python
menu = {
    'Pizza':40,
    'Burger':30,
    'Sandwich':25,
    'Pasta':50,
    'Salad':50,
    'Coffee':35,
}

print("Welcome to Py Cafe")
print("Here's the menu. What would you like to have?")

print("Pizza: $40\n Burger: $30\n Sandwich: $25\n Pasta: $50\n Salad: $50\n Coffee: $35")

order_total = 0

while True:
    item1 = input("Enter the name of item you want to order: ").title()

    if item1 in menu:
        quantity = int(input(f"How many {item1} would you like to have?: "))
        order_total += menu[item1] * quantity
        print(quantity, item1, "has been added to your order")

    else:
        print(f"Sorry! Ordered item {item1} is not available in the menu!")

    another = input("Would you like to order anything else? (yes/no): ").lower()
    if another != 'yes':
        break  

print(f"\nYour total bill amount is: ${order_total}")
print("Thank you for visiting Py Cafe! 😊")
```

---

## ▶ How to Run

1. Install Python (if not installed)
2. Save the script as **py_cafe.py**
3. Run the program:

```bash
python py_cafe.py
```

---

##  Project Structure

```
Py-Cafe/
│── py_cafe.py
│── README.md
```

---



##  Thank You

## Author
Sabin Tiwari

sabintiwari443@gmail.com
