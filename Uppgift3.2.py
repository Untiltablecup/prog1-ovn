årskort = float(input("Hur mycket kostar åskort?"))
biljett = float(input("Hur mycket kostar en biljett?"))
y = int(input("Hur många gånger går du på gymmet per år?"))

x = biljett * y

if årskort < x:
    print ("Det är värt att köpa årskort")
else:
    print ("Det är inte värt att köpa årskort")
