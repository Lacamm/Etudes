from random import randint

def differenciel(releve):
    difference = []
    for n in range(len(releve)):
        difference.append(abs(releve[n] - releve[n-1]))
        
    return difference

releve = []
for n in range(12):
    releve.append(randint(0,70))

print(releve)
print(differenciel(releve))