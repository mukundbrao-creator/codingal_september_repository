rows = int(input("Please enter the number of rows: "))
number = 1

for i in range (1, rows + 1):
    for j in range (1, i + 1):
        print(number, end=" ")
        number = number + 1
    print()
space = 1
for i in range (1, halfDiamRow):
    for j in range (1, space + 1):
        print(end=" ")