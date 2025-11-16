menu = {
    'Pizza':40,
    'Burger':30,
    'Sandwich':25,
    'Pasta':50,
    'Salad':50,
    'Coffee':35,
}

#Greet the customer
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

    