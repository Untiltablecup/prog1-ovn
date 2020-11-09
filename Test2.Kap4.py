import random

y = "go"
x = input ("Rulla tärning? A = [Ja] B = [Nej]")
if x == "A":
    while y == "go":
        n = random.randint (1, 6)
        print (n)
        y = input ("Again?")
        if y == "no":
            break
        else:
            y = "go"

else: 
    print ("No")

