# Make sure art.py is in the same directory

import random
import art

print(art.logo)

attempts = 0

def random_number():
    a = random.randint(1,100)
    return a

def start_again():
    users_answer = input("Do you want to start new game?(yes/no): ")
    if users_answer == "yes":
        level()
    elif users_answer == "no":
        print("Good luck, bye!")

def logic():
    global attempts, a
    guess = int(input("Make a guess: "))
    if guess == a:
        print(f"You got it! The answer was {guess}.")
        start_again()
        return
    elif guess > 100:
        print("You need to write numbers between 1 and 100")
    elif guess > a:
        print("Too high.")
        attempts -= 1
    elif guess < a:
        print("Too low.")
        attempts -= 1

    if attempts == 0:
        print("You've run out of guesses, you lose.")
        start_again()
        return
    elif attempts > 0:
        logic()

def level():
    global attempts, a
    level_choosing = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level_choosing == "easy":
        attempts = 10
        print("You have 10 attempts remaining to guess the number.")
        a = random_number()
        logic()
    elif level_choosing == "hard":
        attempts = 5
        print("You have 5 attempts remaining to guess the number.")
        a = random_number()
        logic()
    else:
        print("Invalid input, please try again!")
        level()
level()
