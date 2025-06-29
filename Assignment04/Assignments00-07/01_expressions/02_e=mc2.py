# Constant for the speed of light in meters per second
C = 299_792_458  # m/s

print("Einstein's Mass-Energy Equivalence Calculator")
print("Enter a negative number to quit.\n")

while True:
    try:
        mass_input = input("Enter kilos of mass: ")
        mass = float(mass_input)

        if mass < 0:
            print("Exiting the program. Goodbye!")
            break

        print("\ne = m * C^2...\n")
        print(f"m = {mass} kg")
        print(f"C = {C} m/s")

        energy = mass * C**2
        print(f"\n{energy} joules of energy!\n")

    except ValueError:
        print("Please enter a valid numeric mass value.\n")
