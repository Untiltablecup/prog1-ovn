import random

guess = 0
guesses = 0
number = random.randint (1, 2)

while guess != number:
    guesses += 1
    guess = random.randint (0, 100000000)
print (f"Amount of tries: {guesses} ")
print (f"The number was: {number}")