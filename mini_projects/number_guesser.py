import random

max_number = input("Enter maximum number: ")

# Check if the entered number is valid
if max_number.isdigit():
    max_number = int(max_number)
else:
    print("Invalid!")
    quit()

# Generate random number
random_number = random.randint(0, max_number)
guesses = 0

while True:
    number = input("Guess the number: ")
    guesses += 1

    # Check if the number is valid
    if number.isdigit():
        number = int(number)

        # Break loop when number is correct
        if number == random_number:
            print("Corect !!")
            break
        else:
            continue
    else:
        print("Invalid number")
        continue

print(f"You guessed {guesses} times")