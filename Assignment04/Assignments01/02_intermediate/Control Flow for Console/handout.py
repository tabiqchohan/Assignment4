import random

print("Welcome to the High-Low Game!")

# Ask the user how many rounds they want to play
rounds = int(input("How many rounds would you like to play? "))
score = 0  # Track the user's score

for round_num in range(1, rounds + 1):
    print(f"\nRound {round_num}:")
    
    # Generate random numbers
    your_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)

    print(f"Your number is: {your_number}")
    guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
    
    # Determine the correct answer
    if your_number > computer_number:
        correct_answer = "higher"
    elif your_number < computer_number:
        correct_answer = "lower"
    else:
        correct_answer = "equal"  # Rare, but possible if numbers are the same

    print(f"The computer's number was: {computer_number}")

    if guess == correct_answer:
        print("You were right! You get a point.")
        score += 1
    elif correct_answer == "equal":
        print("The numbers were equal! No points this round.")
    else:
        print("You were wrong.")

# Final score
print(f"\nGame over! Your total score: {score} out of {rounds}")
