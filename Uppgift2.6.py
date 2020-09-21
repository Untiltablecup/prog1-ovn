inmatning = int (input("Skriv sekunder: ")) #läser in sekunder
sek = int (inmatning) #gör svar till heltal
vecka = sek // 604800
sek = sek % 604800
dag = sek // 86400
sek = sek % 86400
tim = sek // 3600 #delar sekunder med hur många sekunder på en timme, kapar till heltal med //
sek = sek % 3600 #räknar ut antal sekunder som blev över från timmar med modulo
min = sek // 60 #delar resten av sekunderna med hur många sekunder som finns på 1 minut
sek = sek % 60 #räknar ut antal sekunder som blev över från minuter medd modulo

print(f"Vecka: {vecka} \nDag: {dag} \nTimar: {tim} \nMinuter: {min} \nSekunder: {sek}")
