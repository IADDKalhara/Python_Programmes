# =============================     HANGMAN     ============================
# --------------------------------------------------------------------------
# Guess the word 

import random
from words import words


def get_valid_word(words):
    word = random.choice(words)     # Randomly choose a word from a list

    # Choose a valid word without space or dashes
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)        # Createa list from letters of the secret word
    used_letters = set()            # Create a set to store user guessed letters

    lives = len(word) + 5

    while len(word_letters) > 0 and lives > 0:        # Exit loop when the number of letters in word_letters set becomes 0
        user_letter = input("Enter a letter: ").upper()

        # Get a valid input from user
        if user_letter.isalpha() == False or len(user_letter) > 1:
            print("Invalid input, enter valid letter")
            continue
        else:
            # check if user already entered this letter
            if user_letter not in used_letters:
                used_letters.add(user_letter)
            else:
                print("You already guessed this letter, try again.")
            
            lives -= 1

        word_list = [letter if letter in used_letters else "-" for letter in word]          # Add dashes to represent letters in the word user guessed

        print("Current word: "," ".join(word_list) )
        print("You have guessed,"," ".join(used_letters))
        print(f"You have {lives} lives")

        word_letters.discard(user_letter)       # Discard the letter from word list
    
    # Final output of user archievement
    if lives == 0:
        print(f"Sorry, you died. Word was {word}")
    else:
        print("CONGRATULATIONS, YOU WON !!")


hangman()
