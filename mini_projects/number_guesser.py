# ==========================    Number Guesser  =================================
# ===============================================================================
# Computer guessing my number

import random

lowest = 0
highest = int(input("Enter high number: "))

while True:
    number = random.randint(lowest, highest)

    answer = input(f"Is the number {number} too high(H), too low(L) or correct(C)?").lower()

    if answer == "c":
        print(f"Guessed number {number} correctly !")
        quit()
    elif answer == "h":
        highest = number
        continue
    elif answer == "l":
        lowest = number
        continue