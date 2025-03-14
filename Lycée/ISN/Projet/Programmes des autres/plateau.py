###GÉNÉRATION DU PLATEAU DE JEU###


from random import *
import pprint

plateau = [[0 for x in range (16)] for y in range(16)]
plateau[0][0]=3
plateau[15][15]=5


x1 = randint(0, 14)
y1 = randint(0, 14)
while x1 in range(3) and y1 in range(3) or x1 in range(11, 14) and y1 in range(11,14):
        x1 = randint(0, 14)
        y1 = randint(0, 14)
#Exclu les cases de départs du joueur et du bot et celles juste à côtés
plateau[x1][y1]=1
plateau[x1+1][y1]=1
plateau[x1][y1+1]=1
plateau[x1+1][y1+1]=1
x2 = randint(0, 14)
y2 = randint(0, 14)
while x2 in range(3) and y2 in range(3) or x2 in range(11, 14) and y2 in range(11,14) or x1==x2 or x1==x2+1 and y2==y1 or y2==y1+1:
	x2 = randint(0, 14)
	y2 = randint(0, 14)
#Exclu les cases de départs du joueur et du bot et celles juste à côtés et le mur précédent
plateau[x2][y2]=1
plateau[x2+1][y2]=1
plateau[x2][y2+1]=1
plateau[x2+1][y2+1]=1
x3 = randint(0, 14)
y3 = randint(0, 14)
while x3 in range(3) and y3 in range(3) or x3 in range(11, 14) and y3 in range(11,14) or x3==x1 or x3==x1+1 and y3==y1 or y3==y1+1 or x3==x2 or x3==x2+1 and y3==y2 or y3==y2+1:
    x3 = randint(0, 14)
    y3 = randint(0, 14)
plateau[x3][y3]=1
plateau[x3+1][y3]=1
plateau[x3][y3+1]=1
plateau[x3+1][y3+1]=1
x4 = randint(0, 14)
y4 = randint(0, 14)
while x4 in range(3) and y4 in range(3) or x4 in range(11, 14) and y4 in range(11,14) or x4==x1 or x4==x1+1 and y4==y1 or y4==y1+1 or x4==x2 or x4==x2+1 and y4==y2 or y4==y2+1 or x4==x3 or x4==x3+1 and y4==y3 or y4==y3+1:
    x4 = randint(0, 14)
    y4 = randint(0, 14)
plateau[x4][y4]=1
plateau[x4+1][y4]=1
plateau[x4][y4+1]=1
plateau[x4+1][y4+1]=1


    

#Initialisation d'un plateau 16*16 à l'aide d'une liste de listes d'entiers
#Correspondance des entiers avec le type de case :
#0 = neutre 
#1 = mur
#2 = joueur
#3 = joueur confirmé
#4 = bot
#5 = bot confirmé
#6 = drop
#7 = leurre



###CALCUL DE SITUATION###

def calcul_situation(plateau):

    S1 = (sum(x.count(2) for x in plateau[0:16])+sum(x.count(3) for x in plateau[0:16]))
    #Compte le nombre de 2 et de 3 à l'intérieur de toutes les listes de plateau et assigne la somme des deux résultats à S1
    S2 =(sum(x.count(4) for x in plateau[0:16])+sum(x.count(5) for x in plateau[0:16]))
    #Compte le nombre de 4 et de 5 à l'intérieur de toutes les listes de plateau et assigne la somme des deux résultats à S2
    del(plateau[16:])
    plateau.insert(17,S1)
    plateau.insert(18,S2)



###AVANCEMENT###

plateauJ = [[0 for x in range (16)] for y in range(16)]
def avancement_joueur(plateau):
        for row_num in range(16):
                row=plateau[row_num]
                for column in range(16):
                    if row[column] == 2:
                        plateauJ[row_num][column]=2
                        if column-1 >= 0 and plateau[row_num][column-1]==0 or plateau[row_num][column-1]==6 or plateau[row_num][column-1]==7:
                            plateauJ[row_num][column-1]=2
                        if column+1 < 16 and plateau[row_num][column+1]==0 or plateau[row_num][column+1]==6 or plateau[row_num][column+1]==7:
                            plateauJ[row_num][column+1]=2
                        if column-1 >= 0 and plateau[row_num-1][column]==0 or plateau[row_num-1][column]==6 or plateau[row_num-1][column]==7:
                            plateauJ[row_num-1][column]=2
                        if column+1 < 16 and plateau[row_num+1][column]==0 or plateau[row_num+1][column]==6 or plateau[row_num+1][column]==7:
                            plateauJ[row_num+1][column]=2
                    elif row[column] == 3:
                        plateauJ[row_num][column]=3
                        if column-1 >= 0 and plateau[row_num][column-1]==0 or plateau[row_num][column-1]==6 or plateau[row_num][column-1]==7:
                            plateauJ[row_num][column-1]=2
                        if column+1 < 16 and plateau[row_num][column+1]==0 or plateau[row_num][column+1]==6 or plateau[row_num][column+1]==7:
                            plateauJ[row_num][column+1]=2
                        if column-1 >= 0 and plateau[row_num-1][column]==0 or plateau[row_num-1][column]==6 or plateau[row_num-1][column]==7:
                            plateauJ[row_num-1][column]=2
                        if column+1 < 16 and plateau[row_num+1][column]==0 or plateau[row_num+1][column]==6 or plateau[row_num+1][column]==7:
                            plateauJ[row_num+1][column]=2


                

plateauB = [[0 for x in range (16)] for y in range(16)]
def avancement_bot(plateau):
    for row_num in range(16):
        row=plateau[row_num]
        for column in range(16):
            if row[column] == 4:
                plateauB[row_num][column]=4
                if column-1 >= 0 and plateau[row_num][column-1]==0 or plateau[row_num][column-1]==6 or plateau[row_num][column-1]==7:
                    plateauB[row_num][column-1]=4
                if column+1 < 16 and plateau[row_num][column+1]==0 or plateau[row_num][column+1]==6 or plateau[row_num][column+1]==7:
                    plateauB[row_num][column+1]=4
                if column-1 >= 0 and plateau[row_num-1][column]==0 or plateau[row_num-1][column]==6 or plateau[row_num-1][column]==7:
                    plateauB[row_num-1][column]=4
                if column+1 < 16 and plateau[row_num+1][column]==0 or plateau[row_num+1][column]==6 or plateau[row_num+1][column]==7:
                    plateauB[row_num+1][column]=4
            elif row[column] == 5:
                plateauB[row_num][column]=5
                if column-1 >= 0 and plateau[row_num][column-1]==0 or plateau[row_num][column-1]==6 or plateau[row_num][column-1]==7:
                    plateauB[row_num][column-1]=4
                if column+1 < 16 and plateau[row_num][column+1]==0 or plateau[row_num][column+1]==6 or plateau[row_num][column+1]==7:
                    plateauB[row_num][column+1]=4
                if column-1 >= 0 and plateau[row_num-1][column]==0 or plateau[row_num-1][column]==6 or plateau[row_num-1][column]==7:
                    plateauB[row_num-1][column]=4
                if column+1 < 16 and plateau[row_num+1][column]==0 or plateau[row_num+1][column]==6 or plateau[row_num+1][column]==7:
                    plateauB[row_num+1][column]=4





for i in range(1+accélérateur_de_case_joueur):
    avancement_joueur(plateau)
plateau=plateauJ

for i in range(1+accélérateur_de_case_bot):
    avancement_bot(plateau)
plateau=plateauB    

avancement_joueur(plateau)







####OBJETS####

  ##BOMBES##




    bombe_x=bombe[1]
    bombe_y=bombe[2]
    plateau[bombe_x][bombe_y]=0
    if bombe_y-1 >=0 and plateau[bombe_x][bombe_y-1]==4 or plateau[bombe_x][bombe_y-1]==2 or plateau[bombe_x][bombe_y-1]==6 or plateau[bombe_x][bombe_y-1]==7:
        plateau[bombe_x][bombe_y-1]=0
    if bombe_y+1 < 16 and plateau[bombe_x][bombe_y+1]==4 or plateau[bombe_x][bombe_y+1]==2 or plateau[bombe_x][bombe_y+1]==6 or plateau[bombe_x][bombe_y+1]==7:
        plateau[bombe_x][bombe_y+1]=0
    if bombe_x+1 < 16 and plateau[bombe_x+1][bombe_y]==4 or plateau[bombe_x+1][bombe_y]==2 or plateau[bombe_x+1][bombe_y]==6 or plateau[bombe_x+1][bombe_y]==7:
        plateau[bombe_x+1][bombe_y]=0
    if bombe_x-1 >=0 and plateau[bombe_x-1][bombe_y]==4 or plateau[bombe_x-1][bombe_y]==2 or plateau[bombe_x-1][bombe_y]==6 or plateau[bombe_x-1][bombe_y]==7:
        plateau[bombe_x-1][bombe_y]=0
    if bombe_x-1 >=0 and bombe_y+1 < 16 and plateau[bombe_x-1][bombe_y+1]==4 or plateau[bombe_x-1][bombe_y+1]==2 or plateau[bombe_x-1][bombe_y+1]==6 or plateau[bombe_x-1][bombe_y+1]==7:
        plateau[bombe_x-1][bombe_y+1]=0
    if bombe_x+1 < 16 and bombe_y+1 < 16 and plateau[bombe_x+1][bombe_y+1]==4 or plateau[bombe_x+1][bombe_y+1]==2 or plateau[bombe_x+1][bombe_y+1]==6 or plateau[bombe_x+1][bombe_y+1]==7:
        plateau[bombe_x+1][bombe_y+1]=0
    if bombe_x-1 >=0 and bombe_y-1 >=0 and plateau[bombe_x-1][bombe_y-1]==4 or plateau[bombe_x-1][bombe_y-1]==2 or plateau[bombe_x-1][bombe_y-1]==6 or plateau[bombe_x-1][bombe_y-1]==7:
        plateau[bombe_x-1][bombe_y-1]=0
    if bombe_x+1 <16 and bombe_y-1 >=0 and plateau[bombe_x+1][bombe_y-1]==4 or plateau[bombe_x+1][bombe_y-1]==2 or plateau[bombe_x+1][bombe_y-1]==6 or plateau[bombe_x+1][bombe_y-1]==7:
        plateau[bombe_x+1][bombe_y-1]=


		##CASES##

        case_x=case_supplémentaire[2]
        case_y=case_supplémentaire[3]
        if tour[0]=tour[1]
            plateau[case_x][case_y]=2
        elif tour[0]=tour[1]-1
            plateau[case_x][case_y]=4


 ##PLACEMENT DES LEURRES/DROPS##


        leurre_x=leurre[1]
        leurre_y=leurre[2]
        plateau[leurre_x][leurre_y]=7



        drop_x=drop[1]
        drop_y=drop[2]
        plateau[drop_x][drop_y]=6
            
        
        
            






















































