print("===== CALCULATOR =====")
print("Here, you can do addition, subtraction, multiplication, and division with two numbers.\n")
def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

while True:
    try:
        user_input = int(input("Select 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))
    except ValueError:
        print(("Please select 1, 2, 3, or 4 in numerical format. (ex. 1), not ''one''.\n"))
        user_input = int(input("Select 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))
    if user_input == 1:
        try: 
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = addition(num1, num2)
            print(f"{num1} + {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format: (ex. 1), not as ''one''.\n")
    elif user_input == 2:
        try:
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = subtraction(num1, num2)
            print(f"{num1} - {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format: (ex. 1), not as ''one''.\n")
    elif user_input == 3:
        try:
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = multiplication(num1, num2)
            print(f"{num1} * {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format: (ex. 1), not as ''one''.\n")
    elif user_input == 4:
        try: 
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = division(num1, num2)
            print(f"{num1} - {num2} = {result}\n")
        except ZeroDivisionError:
            print("Division by zero is not allowed in mathematics.\n")
        except ValueError:
            print("Please type the numbers in numerical format: (ex. 1), not as ''one''.\n")
    else:
        print("Please select 1, 2, 3, or 4 in numerical format. (ex. 1), not ''one''.\n")
    escape = input("Do you want to stop calculating? (yes or no): ").lower().strip()
    if escape == "yes":
        break
print("===== CALCULATING SESSION COMPLETE =====\n")
print("Have a wonderful day!")