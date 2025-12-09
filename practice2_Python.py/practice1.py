# number guessing game

import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess the number (1–50): "))


    if guess == number:
        print("🎉 Correct! You won!")
        break
    elif guess < number:
        print("Too Low!")
    else:
        print("Too High!")
