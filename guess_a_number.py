import random

while True:
    try:
        
        usernumber = int(input("Guess a number, 1 through 100... "))

        while usernumber != random.randrange(1,101):
            print(int(input("Try again: ")))
        else:
            print("Congratulations, You've guessed correctly!")
            input()

    except ValueError:
        print("Invalid Input")
