starthöjd = int (input("Vad är starthöjden i m?"))
höjd = 0
höjd = starthöjd * 100
studs = 0
while höjd > 1:
    höjd = höjd * 0.7
    studs = studs + 1 
print (f"Bollen studsade {studs: .1f} gånger")