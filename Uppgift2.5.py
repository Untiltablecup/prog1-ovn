svar = input ('Vad är varans pris med moms?')

x = int (svar)

m = 0.25

mp = x * m

p = x - mp

print (f'Utan moms {p: .2f}')

print (f'Momsen {mp: .2f}')