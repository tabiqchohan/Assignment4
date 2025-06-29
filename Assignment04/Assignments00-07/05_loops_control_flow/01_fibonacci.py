# Define the maximum limit as a constant
MAX_VALUE = 10000

# Initialize the first two terms
a, b = 0, 1

# Print Fibonacci numbers while less than MAX_VALUE
while a < MAX_VALUE:
    print(a, end=' ')
    a, b = b, a + b
