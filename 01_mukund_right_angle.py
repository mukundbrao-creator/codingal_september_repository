print("Half Pyramid of Stars (*)")
n = int(input("Give me the number of rows: (ex. 1, 2, 3...) "))
for i in range (n):
    for j in range (i+1):
        print("* ", end="")
    print()