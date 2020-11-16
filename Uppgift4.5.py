while True:
    fortsätt = input("Vill du fortsätta?\n[ja]\n[nej]\n>>> ")
    if fortsätt == "ja":
        starthöjd = int (input("Vad är starthöjden i m?\n>>> "))
        if starthöjd < 0:
            print("ERROR: Starthöjd kan inte vara mindre än 0!\n-------------------------------")
            break
        else:
            höjd = starthöjd * 100
            studs = 0
            while höjd > 1:
                höjd = höjd * 0.7
                studs = studs + 1 
            print (f"Bollen studsade {studs: .1f} gånger!\n-------------------------------")
    elif fortsätt == "nej":
        print("Hejdå!")
        break
    else:
        print("Vänligen välj ja eller nej!\n-------------------------------")
        continue
