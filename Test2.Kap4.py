import random
import time

y = "go"
x = input ("Rulla tärning? A = [Ja] B = [Nej]")
if x == "A":
    while True:
        n = random.randint (1, 6)
        print (n)
        y = input ("Again?")
        time.sleep(1)
        if y == "no":
            break
        else:
            continue

else: 
    print ("No")

