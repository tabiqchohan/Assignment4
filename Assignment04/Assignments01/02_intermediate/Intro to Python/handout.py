# Prompt the user for their Earth weight
earth_weight = float(input("Enter your weight on Earth (in kg): "))

# Calculate weight on Mars (37.8% of Earth weight)
mars_weight = earth_weight * 0.378

# Round the result to 2 decimal places
mars_weight_rounded = round(mars_weight, 2)

# Display the result
print(f"Your weight on Mars would be: {mars_weight_rounded} kg")
