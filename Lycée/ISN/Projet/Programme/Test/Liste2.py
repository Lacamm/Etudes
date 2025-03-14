from random import randint

a = ['a','b','c','d']
b = []
c = []
d = []

oui = randint(1,3)

if  oui == 1:
  b = a
elif oui == 2:
  c = a
elif oui == 3:
  d = a

print(b)
print(c)
print(d)
