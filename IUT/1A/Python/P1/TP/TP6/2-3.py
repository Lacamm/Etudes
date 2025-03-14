from random import randint

def cumulDepuisJanvier(releve):
    total = 0
    cumulJanvier = []
    for n in range(len(releve)):
        total += releve[n]
        cumulJanvier.append(total)
    return cumulJanvier

releve = []
for n in range(12):
    releve.append(randint(0,70))


print(cumulDepuisJanvier(releve))