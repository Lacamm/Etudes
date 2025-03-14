import math

a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

def second_degres(a,b,c):
    delta = (b**2)-(4*a*c)
    print(delta)
    
    if delta < 0:
        print("Il n'y a pas de solutions pour ",a,'x^2+',b,'x+',c,'=0')
    elif delta == 0:
        sol0 = (-b)/(2*a)
        print("Il y a 1 seule solution pour ",a,'x^2+',b,'x+',c,'=0')
        print("Il s'agit de x= ",sol0)
    else:
        sol1 = (-b-(math.sqrt(delta)))/(2*a)
        sol2 = (-b+(math.sqrt(delta)))/(2*a)
        print("Il y a 2 solutions pour ",a,'x^2+',b,'x+',c,'=0')
        print("Il s'agit de x= ",sol1,' et x=',sol2)
    
second_degres(a,b,c)
