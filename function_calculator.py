print("===== FUNCTION CALCULATOR =====")

def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

try:
    user_input = int(input("Type 1 to add, 2 to subtract, 3 to multiply, and 4 to divide: "))
except ValueError:
    print(("Please type 1, 2, 3, or 4 in numerical format. For example, do not type ''one''.\n"))
    user_input = int(input("Type 1 to add, 2 to subtract, 3 to multiply, and 4 to divide: "))
while True:
    if user_input == 1:
        try: 
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = addition(num1, num2)
            print(f"{num1} + {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format. For example, do not type ''one''.\n")
    elif user_input == 2:
        try:
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = subtraction(num1, num2)
            print(f"{num1} - {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format. For example, do not type ''one''.\n")
    elif user_input == 3:
        try:
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = multiplication(num1, num2)
            print(f"{num1} * {num2} = {result}\n")
        except ValueError:
            print("Please type the numbers in numerical format. For example, do not type ''one''.\n")
    elif user_input == 4:
        try: 
            num1 = float(input("Enter the first number. "))
            num2 = float(input("Enter the second number. "))
            result = division(num1, num2)
            print(f"{num1} - {num2} = {result}\n")
        except ZeroDivisionError:
            print("Division by zero is not allowed in mathematics.\n")
        except ValueError:
            print("Please type the numbers in numerical format. For example, do not type ''one''.\n")
    else:
        print("\nPlease type 1, 2, 3, or 4 in numerical format. For example, do not type ''one''.\n")
    escape = input("Do you want to stop calculating? (yes or no): ").lower().strip()
    if escape == "yes":
        break
    else:
        user_input = int(input("Type 1 to add, 2 to subtract, 3 to multiply, and 4 to divide: "))
print("===== CALCULATING SESSION COMPLETE =====\n")
print("Have a wonderful day!")