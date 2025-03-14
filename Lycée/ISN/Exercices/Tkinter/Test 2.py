from tkinter import * #### La fonction précède le programme #####

def change2():                      #On définit la fonction qui va changer le bouton et le label
    L.config(text='BOUM', fg='red')
    B.config(text="J'avais prévenu")

#### Corps  du programme #####
fenetre=Tk()         #On crée la fenêtre                     
fenetre.title('TEST')  #On affiche le titre
L=Label(fenetre, text='ATTENTION DANGER', fg='blue', width=30) #On place et définit le label
L.pack() #On affiche le label
B=Button(fenetre,text="Surtout n'appuyez pas sur le bouton",width=30,command=change2)  #On place et définit le bouton
B.pack()  #On affiche le bouton
fenetre.mainloop() #Impératif sur Tkinter
