"""This is number guessing game 
"""

import random

def start_game():
    min = 1
    max = 10
    max_guess_count = 3
    random_number = random.randint(min, max)
    guessd = False
    for guess_count in range (max_guess_count):
        guess_number = int(input(f"Enter number between {min} and {max}:"))
        if random_number == guess_number:
            print("Great you have guessed the number correctly")
            guessd = True
            break
        elif guess_number > random_number :
            print("You are close think a little downwards")
        elif guess_number < random_number:
            print("You are close think a little upwards")
    if not guessd:
        print("You have lost! Better Luck Next Time")
#print(__name__)
if __name__ == '__main__':
    start_game()
