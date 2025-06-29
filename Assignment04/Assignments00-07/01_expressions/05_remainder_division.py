print("Division and Remainder Calculator\n")

try:
    dividend_input = input("Please enter an integer to be divided: ")
    dividend = int(dividend_input)

    divisor_input = input("Please enter an integer to divide by: ")
    divisor = int(divisor_input)

    if divisor == 0:
        print("You can't divide by zero!")
    else:
        quotient = dividend // divisor
        remainder = dividend % divisor

        print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

except ValueError:
    print("Please enter valid integers.")
