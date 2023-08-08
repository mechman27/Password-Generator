from art import logo
import os

def add(num1, num2):
    return num1 + num2
def multiply (num1, num2):
   return num1 * num2
def divide (num1, num2):
    return num1 / num2
def subtract (num1, num2):
    return num1 * num2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    first_num = float(input("Please select your first number: "))
    result = 0
    is_done = False
    while not is_done: 
        operator = input("[+, -, /, *] Please select an operator: ")
        second_num = float(input("Please select your second number: "))
        if operator not in operations:
            print("Please enter a valid operator")
        else:
            calculation = operations[operator]
            result = calculation(first_num, second_num)
            print (f"{first_num} {operator} {second_num} = {result}")
            end_choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation or press enter to quit: ").lower()
            if end_choice == "y":
                first_num = result
            elif end_choice == "n":
                os.system("clear")
                calculator()
            else:
                print("Thank you for playing. Goodbye.")
                is_done = True

calculator()