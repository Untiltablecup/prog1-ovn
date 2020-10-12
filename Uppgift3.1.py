tid = float(input("Hur många minuter per månad?"))
peng = float(input("Hur mycket kr per min?"))

x = tid * peng

if x >= 300:
    x = x * 0.9
else: 
    x = x
print (f"Det blir: {x: .2f}kr")