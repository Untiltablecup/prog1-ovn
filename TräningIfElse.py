morning = input("What you do during morning before school? Choose between: Sleeping, Eating breakfast, Nothing, Looking at mail and schoolsoft ")

if morning == "Sleeping":
    print ("Maybe not? So you don't get late to school!")
elif morning == "Eating breakfast":
    print ("Why though?")
elif morning == "Nothing":
    print ("K")
elif morning == "Looking at mail and schoolsoft":
    print ("Good for you. You might not have to go to school!")
    school = input("Did you have to go to school today?")
    if school == "Yes": 
        print ("Aww big rip")
    else :
        print ("Yay")
else :
    print ("Why didn't you choose a answer?")