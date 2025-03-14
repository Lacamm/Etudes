from random import randint

def cumulPrecipitations(releve):
    return sum(releve)

releve = []
for n in range(12):
    releve.append(randint(0,70))


print(cumulPrecipitations(releve))