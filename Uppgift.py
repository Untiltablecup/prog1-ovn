tal = input ("Skriv ett heltal?")
tal = float (tal)

svar = tal % 2

if svar == 1:
    print(f"Talet {svar} är ojämnt")
else :
    print(f"Talet {svar} är jämt")
