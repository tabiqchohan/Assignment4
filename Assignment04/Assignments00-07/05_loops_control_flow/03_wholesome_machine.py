# The affirmation the user must type
affirmation = "I am capable of doing anything I put my mind to."

# First prompt
print(f"Please type the following affirmation: {affirmation}")

# Loop until user types the affirmation exactly
while True:
    user_input = input()
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation.")
        print(f"Please type the following affirmation: {affirmation}")
