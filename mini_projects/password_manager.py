from cryptography.fernet import Fernet

print("=====================================")
print("         PASSWORD MANAGER            ")
print("=====================================")


def add():
    name = input("Account name: ")
    password = input("Password: ")

    # Open file in append mode
    with open("passwords.txt", "a") as f:
        f.write(name + "," + fer.encrypt(password.encode()).decode() + "\n")


# Get the encrypt key generated
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# Get master password from user and combine it with encryption key
master_password = input("Enter Master Password: ")
key = load_key() + master_password.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        # Read file line by line and print
        for line in f.readlines():
            line = line.rstrip()
            user, password = line.split(",")
            print(f"Username: {user} | Password: {fer.decrypt(password.encode()).decode()}")

# This is a one time use function
# Generate a encrypt key and put it in a key file
'''
def write_key():
    encrypt_key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(encrypt_key)
'''


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


