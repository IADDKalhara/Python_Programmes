####    Simple Calculator   ####

# Functions for arithmatic operations and output
def add(a, b):
    print(f"{a} + {b} = {a + b}")
    return

def subtract(a, b):
    print(f"{a} - {b} = {a - b}")
    return

def multiply(a, b):
    print(f"{a} * {b} = {a * b}")
    return

def divide(a, b):
    try:
        print(f"{a} / {b} = {a / b}")
        return
    except ZeroDivisionError:
        print("float division by zero")
        print(f"{a} / {b} = None")


def power(a, b):
    total = 0

    for i in range(b + 1):
        total += a * i
    
    print(f"{a} ^ {b} = {total}")
    return

def remainder(a, b):
    print(f"{a} % {b} = {a % b}")
    return


def select_op(choice):
    # End programme
    if choice == "#":
        return (-1)

    while True:
        try:
            first_number = input("Enter first number: ")
            print(first_number)
            # Reset
            if "$" in first_number:
                break
            # End programme
            if "#" in first_number:
                return (-1)

            second_number = input("Enter second number: ")
            print(second_number)
            if "$" in second_number:
                break
            if "#" in second_number:
                return (-1)

            # Convert string inputs into numbers
            first_number = float(first_number)
            second_number = float(second_number)

        except ValueError:  
            print("Not a valid number,please enter again")

        if choice == "+":
            add(first_number, second_number)
            break
        elif choice == "-":
            subtract(first_number - second_number)
            break
        elif choice == "*":
            multiply(first_number, second_number)
            break
        elif choice == "/":
            divide(first_number, second_number)
            break
        elif choice == "^":
            power(first_number, second_number)
            break
        elif choice == "%":
            remainder(first_number, second_number)
            break
        elif choice == "$":
            break
        else:
            print("Unrecognized operation")
            break
    

while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)

  if(select_op(choice) == -1):
    print("Done. Terminating")
    exit()
