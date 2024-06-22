# Task 1 -- Create functions for each arithmetic operation

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y


# Task 2 -- Implement user input to receive numbers and an operation choice

def calculate():
    x = float(input("Please enter your first number: "))
    y = float(input("Please enter your second number: "))
    
    choice = input("What operation would you like to perform? (+, -, *, /): ")

    if choice == '+':
        print(f"{x} + {y} = {addition(x, y)}")
    elif choice == '-':
        print(f"{x} - {y} = {subtraction(x, y)}")
    elif choice == '*':
        print(f"{x} * {y} = {multiplication(x, y)}")
    elif choice == '/':
        if y == 0:
            print("Error: Division by zero is not allowed!")
        else:
            print(f"{x} / {y} = {division(x, y)}")
    else:
        print("You must choose from only the following operations: '+', '-', '*', or '/'. ")

calculate()