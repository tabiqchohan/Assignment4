MAX_LENGTH = 3

def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print("Removed:", removed)

def main():
    values = []

    num = int(input("How many elements do you want to enter? "))
    for i in range(num):
        value = input(f"Enter value {i + 1}: ")
        values.append(value)

    print("Original list:", values)
    shorten(values)
    print("Final list:", values)

if __name__ == "__main__":
    main()
