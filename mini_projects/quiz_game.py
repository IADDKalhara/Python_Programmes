print("============================")
print("!!!! Welcome to COMQUIZ !!!!")
print("============================")

# In case of user don't want to play or invalid input, exit programme
playing = input("Do you want to continue(yes/no)? ")

if (playing.lower() == "no"):
    print("Ending Programme....")
    quit()
elif (playing.lower() != "yes"):
    print("Invalid input.. Ending programme ...")
    quit()

# when everything ok, continue
print("Okay!.. Let's begin!")
score = 0

answer = input("What is CPU stands for? ")
if (answer.lower() == "central processing unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is GPU stands for? ")
if (answer.lower() == "graphics processing unit"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is RAM stands for? ")
if (answer.lower() == "random access memory"):
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percentage = "{:.2f}".format((score / 3) * 100)
print(f"You got {str(score)} answers correct :) {percentage}%")
