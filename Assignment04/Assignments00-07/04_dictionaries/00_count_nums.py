print("Number Counter\n")
print("Enter numbers one at a time. Press Enter without typing anything to finish.\n")

counts = {}

while True:
    num_input = input("Enter a number: ")
    if num_input.strip() == "":
        break

    try:
        num = int(num_input)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1
    except ValueError:
        print("Please enter a valid integer.")

print("\nCount results:")
for number, count in counts.items():
    print(f"{number} appears {count} times.")
