print("Welcome to the Phonebook!\n")

# Initialize phonebook dictionary
phonebook = {}

while True:
    print("\nOptions:")
    print("1. Add a contact")
    print("2. Look up a contact")
    print("3. View all contacts")
    print("4. Exit")

    choice = input("\nChoose an option (1–4): ")

    if choice == "1":
        name = input("Enter name: ").strip()
        number = input("Enter phone number: ").strip()
        phonebook[name] = number
        print(f"Contact '{name}' added.")

    elif choice == "2":
        name = input("Enter name to look up: ").strip()
        if name in phonebook:
            print(f"{name}'s number is {phonebook[name]}")
        else:
            print(f"{name} not found in phonebook.")

    elif choice == "3":
        if phonebook:
            print("\nPhonebook Entries:")
            for name, number in phonebook.items():
                print(f"{name}: {number}")
        else:
            print("Phonebook is empty.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1–4.")
