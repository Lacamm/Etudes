from tkinter import *

# Définition des fonctions et procédures

def affiche():    

   nom = le_prenom.get()
   age=2017-int(entre_annee.get())                                       #on applique la méthode get() sur l'objet entre_annee  et on calcul 
   texte="Bonjour "+nom+". \n 2017 est l'année de tes "+str(age)+" ans"
   bouton.config(text=texte)                                                                      # Affiche le résultat

# Corps du programme et interface

fen=Tk()

fen.title("SALUT")

prenom = Label(fen, text = "Quel est ton prénom?", font = 'arial')

prenom.pack()

le_prenom = Entry(fen, width = 10, font='arial')

le_prenom.pack()

titre_annee=Label(fen,text="En quelle année es tu né? ",font="arial ")

titre_annee.pack()

entre_annee=Entry(fen, width=6,font="arial ")

entre_annee.pack()

bouton=Button(fen,text="Envoi",bg='grey',fg='white',command=affiche)       #Appel de la fonction affiche

bouton.pack()

fen.mainloop()
