from tkinter import *       # importe la bibliothèque
fen=Tk()          # crée une fenêtre fen
L=Label(fen, text='Ecrivez pour voir', fg='orange')    #crée une étiquette
L.pack()        #Affiche et redimensionne l'étiquette L
E=Entry(fen, fg='purple')       #Crée une zone de saisie E
E.pack()        #affiche la zone de saisie
B=Button(fen, fg='red', text='Au revoir', command=fen.destroy)  #Crée un bouton B
B.pack()       #Affiche le bouton B
B2=Button(fen, fg='lime', text='Et a bientot', command=fen.destroy)
B2.pack()
fen.mainloop()      #Affiche la fenêtre et attend les événements
