print("Leap Year Checker\n")

try:
    year_input = input("Enter a year: ")
    year = int(year_input)

    # Check leap year conditions
    if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

except ValueError:
    print("Please enter a valid integer year.")
