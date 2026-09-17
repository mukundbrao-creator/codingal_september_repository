import random
playing = True
number = str(random.randint(0,9))
print("I will generate one random number from 0-9, and you will have to guess the number one didget at a time.")
print("The game ends when you get 1 hero.")

while playing:
    guess = input("Give me your best guess! ")
    if number == guess:
        print("You win the game.")
        print("The number was:", number)
        break
    else:
        print("You guess isn't quite right. Try again.")