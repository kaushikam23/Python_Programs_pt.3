numbers = []
count = 0
total = 0

while True:
    user_input = input("Enter a number (or 'done' to finish): ")

    if user_input == "done":
        break

    try:
        number = float(user_input)
        numbers.append(number)
        count += 1
        total += number
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if count > 0:
    average = total / count
    print("Count:", count)
    print("Total:", total)
    print("Average:", average)
else:
    print("No numbers were entered.")
