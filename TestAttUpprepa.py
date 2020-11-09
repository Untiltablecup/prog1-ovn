import random

guess = 0
guesses = 0
correct = random.randint(1, 100000)

while guess != correct:
    guesses += 1
    guess = int(input("Gissa på ett tal: "))

    if guess < correct:
        print ("För litet")
    
    elif guess > correct:
        print ("För stort")
print ("Nice, gg wp c:")
print (f"Antal försök = {guesses}")