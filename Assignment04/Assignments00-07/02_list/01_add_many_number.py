def sum_numbers(numbers):
    return sum(numbers)

def main():
    
    input_str = input("Enter numbers separated by spaces: ")
    numbers = list(map(float, input_str.split()))
    
    total = sum_numbers(numbers)
    print("The sum of the numbers is:", total)

if __name__ == "__main__":
    main()


