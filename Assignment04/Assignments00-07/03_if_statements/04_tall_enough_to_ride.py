MIN_HEIGHT = 50  # Minimum height requirement

height_input = input("How tall are you? ")

if height_input.strip() == "":
    print("No height entered. Exiting.")
else:
    try:
        height = float(height_input)
        if height >= MIN_HEIGHT:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")
    except ValueError:
        print("Please enter a valid numeric height.")
