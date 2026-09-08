secret = 50
attempts = 0
while attempts < 5:
    guess = int(input("Guess the secret number: "))
    attempts += 1
    if guess == secret:
        print("You won!")
        break
    difference = abs(secret - guess)
    if difference >= 30:
        print("Ice cold.")
    elif difference >= 15:
        print("Cold.")
    elif difference >= 5:
        print("Warm.")
    else:
        print("Hot.")
    remaining = 5 - attempts
    for i in range (remaining):
        print("❤️", end=" ")
    print()
else:
    print("Game over!")
    print("The secret number was", secret)