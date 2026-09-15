try: 
    num1, num2 = eval(input("Enter two numbers, separated by a comma: "))
    result = num1 / num2
    print("Result is", result)
except ZeroDivisionError:
    print("You cannot divide by 0, it is an error!")
except SyntaxError:
    print("A comma is missing. Please enter two numbers seperated by a comma, like this: 1, 2 ")
except:
    print("Wrong input.")
else: 
    print("No exceptions.")
finally:
    print("This will run no matter what!")


