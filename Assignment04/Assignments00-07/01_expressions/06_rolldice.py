import random

print("Dice Roll Simulator\n")

# Simulate rolling two six-sided dice
die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
total = die1 + die2

# Print results
print(f"Die 1 rolled: {die1}")
print(f"Die 2 rolled: {die2}")
print(f"Total: {total}")
