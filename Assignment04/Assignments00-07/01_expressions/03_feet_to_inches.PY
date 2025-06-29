print("Feet to Inches Converter")
print("Enter a negative number to quit.\n")

while True:
    try:
        feet_input = input("Enter feet: ")
        feet = float(feet_input)

        if feet < 0:
            print("Exiting the program. Goodbye!")
            break

        inches = feet * 12
        unit = "foot" if feet == 1 else "feet"
        print(f"\n{feet} {unit} is {inches} inches.\n")

    except ValueError:
        print("Please enter a valid numeric value.\n")
