#
# Guess the Number
#
# Project developed by Tomás Cardozo
# Start date: 24/8/2021
# Finish date:
# The user needs to guess the right number between 1 and 50 to win the game
# Whenever they guess wrong, it'll ask them if they want to keep playing or just quit
#
#

import random
import os


def screenClear():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
    pass


def tryGuess():
    randomNumber = random.randint(1, 50)
    print(randomNumber)
    attempts = 0
    takeGuess = None
    
    while takeGuess != randomNumber:
        takeGuess = int(input("Guess a number between 1 and 50 "))

        if takeGuess == randomNumber:
            print("Congrats. You won!")
            print("The number was", randomNumber)
            print("You guessed the number in", attempts + 1, "attempts")

        else:
            print("Wrong Number. Keep trying")
            attempts += 1


print("Hey! Welcome to Guess the Number")
print("Please, insert a name down below to start the game")
username = str(input())
print("Ok, let's begin", username)
screenClear()
tryGuess()
