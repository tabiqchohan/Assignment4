# Ask the user for their age
age = int(input("How old are you? "))

# Voting ages in fictional countries
voting_ages = {
    "Peturksbouipo": 16,
    "Stanlau": 25,
    "Mayengua": 48
}

# Check and print voting eligibility
for country, required_age in voting_ages.items():
    if age >= required_age:
        print(f"You can vote in {country} where the voting age is {required_age}.")
    else:
        print(f"You cannot vote in {country} where the voting age is {required_age}.")
