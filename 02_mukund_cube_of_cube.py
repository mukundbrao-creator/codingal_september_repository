def cube_number(number):
    return number*number*number
def by_three(number):
    if number % 3 == 0:
        return cube_number(number)
    else:
        return False
print(by_three(27))
print(by_three(9))