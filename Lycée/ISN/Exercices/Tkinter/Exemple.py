from tkinter import *                                       # importe la bibliothèque
fen=Tk()                                                          # crée une fenêtre fen
L=Label(fen, text='Formation ISN', fg='blue')      #crée une étiquette
L.pack()                                                          #Affiche et redimensionne l'étiquette L
E=Entry(fen,bg='grey')                                     #Crée une zone de saisie E
E.pack()                                                          #affiche la zone de saisie
B=Button(fen,text='Quitter', command=fen.destroy)  #Crée un bouton B
B.pack()                                                         #Affiche le bouton B
fen.mainloop()                                                #Affiche la fenêtre et attend les événements
