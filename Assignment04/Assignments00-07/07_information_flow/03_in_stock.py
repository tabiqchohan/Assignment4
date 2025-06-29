# Sample inventory for demonstration
inventory = {
    'apple': 50,
    'banana': 75,
    'pear': 1000,
    'orange': 30
}

def num_in_stock(fruit):
    """Returns the number of the specified fruit in inventory."""
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ").strip()
    stock = num_in_stock(fruit)

    if stock > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock)
    else:
        print("This fruit is not in stock.")

# Run the main function
if __name__ == "__main__":
    main()
