def main():
    # Create a list called fruit_list
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    # Print the length of the list
    print("Length of fruit list:", len(fruit_list))
    
    # Add 'mango' at the end of the list
    fruit_list.append('mango')
    
    # Print the updated list
    print("Updated fruit list:", fruit_list)

main()

def access_element(lst, index):
    if 0 <= index < len(lst):
        return f"Element at index {index}: {lst[index]}"
    else:
        return "Index out of range!"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        old_value = lst[index]
        lst[index] = new_value
        return f"Replaced '{old_value}' with '{new_value}' at index {index}."
    else:
        return "Index out of range!"

def slice_list(lst, start, end):
    if start < 0 or end > len(lst) or start > end:
        return "Invalid slice indices!"
    return lst[start:end]

def index_game():
    my_list = ['red', 'blue', 'green', 'yellow', 'purple']

    print("Welcome to the Index Game!")
    print(f"Current List: {my_list}")

    while True:
        print("\nChoose an operation: access / modify / slice / quit")
        choice = input("Your choice: ").strip().lower()

        if choice == "access":
            idx = int(input("Enter index to access: "))
            print(access_element(my_list, idx))

        elif choice == "modify":
            idx = int(input("Enter index to modify: "))
            new_val = input("Enter new value: ")
            print(modify_element(my_list, idx, new_val))
            print("Updated List:", my_list)

        elif choice == "slice":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            sliced = slice_list(my_list, start, end)
            print("Sliced list:", sliced)

        elif choice == "quit":
            print("Thanks for playing!")
            break

        else:
            print("Invalid option. Please choose access, modify, slice, or quit.")

# Run the game
index_game()
