# Dictionary of fruits and their prices per unit
fruit_prices = {
    'apple': 3.0,
    'durian': 15.0,
    'jackfruit': 12.5,
    'kiwi': 2.0,
    'rambutan': 7.0,
    'mango': 10.0
}

total_cost = 0.0

# Loop through each fruit and prompt user for quantity
for fruit, price in fruit_prices.items():
    quantity_str = input(f"How many ({fruit}) do you want?: ")
    try:
        quantity = int(quantity_str)
        total_cost += quantity * price
    except ValueError:
        print(f"Invalid input for {fruit}, assuming 0.")

# Print the total cost
print(f"Your total is ${total_cost}")
