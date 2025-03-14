from random import randint

a = randint(0,100)
b = randint(0,100)
c = randint(0,100)
d = randint(0,100)

print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)


def petit(a,b,c,d):
    if a < b:
        res = a
    else:
        res = b
    if c < res:
        res = c
    elif d < res:
        res = d
    return res

print()
print('res=', petit(a,b,c,d))