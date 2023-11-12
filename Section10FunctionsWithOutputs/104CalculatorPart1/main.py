import art
import os

def do_math(first_number, second_number, operator):
    if operator == "+":
        return first_number + second_number
    elif operator == "-":
        return first_number - second_number
    elif operator == "*":
        return first_number * second_number
    elif operator == "/":
        return first_number / second_number
    else:
        return "Please provide a valid operator"



def calculator():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    first_number = False
    operation = "+"
    second_number = "0"
    total = 0
    continueMathing = 'y'
    while continueMathing == 'y':
        if not first_number:
            first_number = float(input("What's the first number?: "))
        else:
            first_number = total
        operation = input("+\n-\n*\n/\nPick an operation: ")
        second_number = float(input("What's the next number?: "))
        total = do_math(first_number, second_number, operation)
        print(f"{first_number} {operation} {second_number} = {total}")
        continueMathing = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
    if (continueMathing == 'n'):
        calculator()    

calculator()