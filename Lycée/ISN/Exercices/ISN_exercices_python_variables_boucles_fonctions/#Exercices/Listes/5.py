#Création liste avec les coefficients qui correspondent aux matières
coeffmatière = [['H-G',3],['maths',7],['P-C',6],['S-I',6],['LV1',3],
                ['LV2',2],['Philo',3],['EPS',2],['INS',2]]
#Création de variables pour calculerla moyenne
notesTT = 0
coeffTT = 0

print("Quelle note espérez vous avoir au Bac") #Affichage de la phrase

#On fera la boucle autant de fois qu'il y a de matières
for i in range(len(coeffmatière)):
    print(coeffmatière[i][0], ': ') #On demande la note en fonction de la matère
    notes = int(input()) #on rentre la note
    #On vérifie que la note est comprise entre 0 et 20, et on recommence tant
    #que la note est incorrecte
    while notes<0 or notes>20:
        print("Note incorrecte")
        print(coeffmatière[i][0], ': ')
        notes = int(input())
    notesTT = notesTT + notes*coeffmatière[i][1] #Somme des notes en tenant compte
    #des coefficiants
    coeffTT = coeffTT + coeffmatière[i][1] #Somme du nombre de note

moyenne = round(notesTT/coeffTT,2) #Calcul de la moyenne
print("Votre moyenne prévisionelle est de: ",moyenne) #Affichage de la moyenne

#On compare la moyenne aux barémes du BAC pour voir quelle mention a été obtenue
if moyenne<8:
    print("Vous êtes recalé")

if moyenne>=8 and moyenne<10:
    print("Vous êtes admis à présenter l'ORAL DE RATRAPPAGE du second groupe")

if moyenne>=10 and moyenne<12:
    print("Vous êtes admis SANS MENTION")

if moyenne>=12 and moyenne<14:
    print("Vous êtes admis avec la mention ASSEZ BIEN")

if moyenne>=14 and moyenne<16:
    print("Vous êtes admis avec la mention BIEN")

if moyenne>=16:
    print("Vous êtes admis avec la mention TRES BIEN")
