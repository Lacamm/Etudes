def nombreChiffres(motDePasse):
    chiffre = False
    caractère = 0
    while not chiffre:
        for cacractère in motDePasse:
            if caractère.isdigit():
                chiffre = True
        print("Votre mot de Passe doit contenir au moins 1 chiffre")
        motDePasse = str(input())
    return motDePasse

motDePasse = str(input())
MDP = []
for n in range(len(motDePasse)):
    MDP.append(motDePasse[n])
#print(nombreChiffres(motDePasse))

assert nombreChiffres(motDePasse)

