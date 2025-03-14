#Fonction
def Anagram(ch1,ch2):
    n = 0
    faux = 0
    chaine = True
    if len(ch1) == len(ch2):   #On vérifie que les deux chaînes ont le même nombre ce caractéres
        for p in range (len(ch1)):
            if ch1[1] != ch2[n]:
                if ch1[1] = ch2[n] == False
                while ch1[1] != ch2[n]: #On vérifie qu'on retrouve bien le même caractère dans les deux liste
                      #On vérifie qu'on ne dépasse pas le rang
                        faux = 1
            else:
                ch1.remove(ch1[1])  #On supprime les éléments vérifiés
                ch2.remove(ch2[n])
                n = 0
                chaine = True
    else:
        chaine = False
    if faux == 0:
        chaine = True
    else:
        chaine = False
    return chaine

#####################
#Programme principal
#####################

#On désigne les variables
ch1 = []
ch2 = []
n = 0
CHAINE = True

#On entre les chaînes de caractères
ch1 = input('ch1:')
ch2 = input('ch2:')

#On affiche le résultat
if CHAINE == Anagram(ch1,ch2):
    print("Ce sont des anagrammes")
else:
    print("Ce ne sont pas de anagrammes")

#J'ai pas eu le temps de faire le 3
