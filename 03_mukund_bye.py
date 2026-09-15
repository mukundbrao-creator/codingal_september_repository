valid = False
while not valid:
    try:
        n = int(input("Enter an even number: "))
        while n%2==0:
            print("bye!")
            valid = True
            n=1
    except ValueError:
        print("Invalid.")