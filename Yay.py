def ja(ok):
    print("ja\n" +str(ok) + " \nhej")
    a=[["d", "f"], ["c", "b"], ["a", "j"]]
    a.sort()
    return a

test = ja(80)

for b in test:
    print(b)

def nej(no):
    if no == ja:
        return "Hej"
    else:
        return "Nope"

print(nej(ja))


def ip():
    i = ['ja', 'ja', 'ja', 'nej', 'kanske']
    return i

kanske = ip()
print(kanske.count('ja'))
kanske.append('ja')
print(kanske)
print(kanske[3])
print(kanske[0:3])

try:
    b = 3/3
    print(k)
except ZeroDivisionError:
    print("Fel, du kan inte dividera med 0!")
except:
    print("Something else went wrong!")

def important_message():
    print("This is a message that is important!")
    hejllo = input("Answer please?" + "\n>")
    print("Hello! " + str(hejllo))

def hello():
    print("Ja")
    return important_message()

hello()

def hj():
    lista = ['1']
    _a = 1
    while _a < 10:
        _a += 1
        lista.append[_a]
    return lista

print(hj())

