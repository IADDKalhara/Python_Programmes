import random

options = ["rock", "paper", "scissors"]

user_wins = 0
computer_wins = 0

while True:
    user_input = input("Enter Rock/Paper/Scissors or Q to quit: ").lower()

    if user_input == "q":
        break

    # Get valid input from user
    if user_input not in options:
        print("Invalid input")
        continue
    
    # rock = 0, paper = 1, scissors = 2
    computer_input = str(random.randint(0, 2))

    if user_input == "rock" and computer_input == "2":
        print("You win!")
        user_wins += 1
    elif user_input == "paper" and computer_input == "0":
        print("You win!")
        user_wins += 1
    elif user_input == "scissors" and computer_input == "1":
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1

print(f"You won {user_wins} times")
print(f"Computer won {computer_wins} times")
print("Goodbye!")