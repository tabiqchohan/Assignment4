def get_first_element(lst):
    # Print the first element of the list
    print("The first element is:", lst[0])

def main():
    lst = []
    num_elements = int(input("How many elements do you want to enter? "))

    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        lst.append(element)

    print("Your list:", lst)
    get_first_element(lst)

if __name__ == "__main__":
    main()
