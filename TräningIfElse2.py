name = input("What's your name?")

print ("It's so nice to meet you", name)

start = input("Do you wanna wake up and start your day? (Yes) (No)")
if start == "Yes":
    print ("*You wake up for your first day at your new school*")
    morning = input("What do you do now?: A = (Eat breakfast) B = (Go straight to school)")

    if morning == "A":
        print ("*You walk into the kitchen and look in the freezer, only to notice that you're all out of food*")
        nofood = input("*You panic* I have no food! What should I do?!: A = (Go straight to school) B = (Go to Kfc)")
        if nofood == "A":
            print ("*You grab your bag and walk to school feeling hungry*")
    elif morning == "B":
        print ("*You quickly grab your bag and run to the closest kfc*")
        print ("*Walking through the doors of kfc you get hit in the face by the smell of fried chicken*")
        print ("*You walk up to the counter and take look at the menu*")
        print ("Person behind the counter: Welcome to kfc! Are you ready to order?")
        food = input("I think I'll order the: A = (Original Recipe Bucket) B = (Hot Wings Bucket) C = (Boneless Bucket)")
        if food == "C":
            print ("*You get your bucket of boneless chicken and run to school*")
            print ("*You get 20min late to school but the teacher doesn't notice*")
            print ("*You start eating your chicken when the person sitting in front of you turns around*")
            kfc = input("???: Is that kfc?: A = (Yes) B = (No)")
            if kfc == "A":
                givekfc = input("???: Ooo I love kfc! May I have some?")




        elif food == "A" or "B":
            print ("*You get to class late and start eating your food*")
            print ("*You choke on a bone from one of the chicken wings and die*")

    else:
        print ("*You fall back asleep and miss the chance to meet the love of your life*")

else:
    print ("You sleep through the day and miss the chance to meet the love of your life")
    print ("I guess you just have to restart")