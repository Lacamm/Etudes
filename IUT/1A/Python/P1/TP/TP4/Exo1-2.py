def position (phrase, mot):
    """
    Cette fonction a pour objectif de déterminer la position d'un mot dans une phrase
    Paramètres:
      para1: la chaîne à tester
      para2: le mot cherché dans la phrase
    Résultat: une liste qui renvoie les positions du mot dans la phrase
    """
    resultat = []
    faux = 0
    vrai = 0

    for n in range(len(phrase)):
        if phrase[n] == mot[0]:
            a = n
            for i in range(len(mot)):
                if phrase[a+i] == mot[i]:
                    vrai = 1
                else:
                    faux = 1
            if phrase[a+i+1] == " ":
                vrai = 1
            else:
                faux = 1
                
            if faux == 0 and vrai == 1:    
                resultat.append(n)
            faux = 0
            vrai = 0        
    return resultat

phrase = str(input("Une phrase: "))
mot = str(input("Le mot à chercher: "))

print(position(phrase,mot))