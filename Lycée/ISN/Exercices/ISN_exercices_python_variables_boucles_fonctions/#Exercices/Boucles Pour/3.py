#On rentre les bornes de l'intervalle
borne1 = int(input("Veuillez entrer la première borne de l'intervalle: "))
borne2 = int(input("Veuillez entrer la seconde borne de l'intervalle: "))

#On vérifie que les bornes de l'intervalle sont dans le bon sens
if borne2<borne1:
    borne2 = borne1
    borne1 = borne2

#On calcule et affiche tout les résultats
for n in range(abs(borne1)+abs(borne2)+1):
    resultat = (2*borne1**2)-(3*borne1)+5
    print('x=',borne1,', f(x)=',resultat)
    borne1 = borne1 +1
