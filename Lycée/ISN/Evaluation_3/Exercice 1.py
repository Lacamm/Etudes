#Fonction
def PGCD(a,b,r):
    r = a/b            #On fait des divisions successives qui vont permettre de trouver un reste nul et du même coup le PGCD qui sera la dernière valeur de b
    while r!= 0:
        a = b
        b = r
        r = a/b
    return b


#####################
#Programme principal
#####################
r = 0

print("Entrez deux valeurs")        #On entre les variables

a = int(input('a = '))
b = int(input('b = '))

print("Le PGCD de",a,'et',b,'est',PGCD(a,b,r))     #On affiche les résultats
