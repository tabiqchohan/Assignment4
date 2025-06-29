ADULT_AGE = 18  # Legal adult age in the United States

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

# Get user input and call the function
age_input = int(input("How old is this person?: "))
print(is_adult(age_input))
