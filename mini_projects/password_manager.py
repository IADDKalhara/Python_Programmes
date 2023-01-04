from cryptography.fernet import Fernet

print("=====================================")
print("         PASSWORD MANAGER            ")
print("=====================================")


def add():
    name = input("Account name: ")
    password = input("Password: ")

    # Open file in append mode
    with open("passwords.txt", "a") as f:
        f.write(name + "," + password + "\n")


def view():
    with open("passwords.txt", "r") as f:
        # Read file line by line and print
        for line in f.readlines():
            line = line.rstrip()
            user, pwd = line.split(",")
            print(f"Username:{user} | Password:{pwd}")

master_password = input("Enter Master Password: ")

while True:
    choice = input("What do you want to do add / view or q to quit)? ").lower()

    if choice == "q":
        quit()
    elif choice == "add":
        # Add a new entry
        add()
        continue
    elif choice == "view":
        # View entries
        view()
        continue
    else:
        print("Invalid input")


