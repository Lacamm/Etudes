from random import choice

l1 =list(range(1,90))

for r in range(89):
    a = choice(l1)
    l1.remove(a)
    print(a)

print('Bingo')
