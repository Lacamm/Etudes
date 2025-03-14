from tkinter import *

# Définition des fonctions et procédures

def affiche():    

   age=2017-int(entre_annee.get())                                                           #on applique la méthode get() sur l'objet entre_annee  et on calcul

   texte="Bonjour . \n 2017 est l'année de tes "+str(age)+" ans"    

   bouton.config(text=texte)                                                                      # Affiche le résultat


# Corps du programme et interface

fen=Tk()

fen.title("SALUT")

titre_annee=Label(fen,text="En quelle année es tu né? ",font="arial ")

titre_annee.pack()

entre_annee=Entry(fen, width=6,font="arial ")

entre_annee.pack()

bouton=Button(fen,text="Envoi",bg='grey',fg='white',command=affiche)       #Appel de la fonction affiche

bouton.pack()

fen.mainloop()
