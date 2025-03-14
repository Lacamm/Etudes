a = 0.88715401

z = int(input('Voulez-vous convertir des dollars (pressez 1) ou des euros (pressez 2)? '))

while z!=1 and z!=2:
    z = int(input('Voulez-vous convertir des dollars (pressez 1) ou des euros (pressez 2)?'))  

if z == 1:
    b = float(input('Valeur en dollar: '))
    c = b/a
    print('Valeur en euro: ',round(c,2),'€')

if z == 2:
    b = float(input('Valeur en euro: '))
    c = a*b
    print('Valeur en dollar: ',round(c,2),'$')
