from tkinter import * #### La fonction précède le programme #####
def change() :
      if B.cget('text')=='JOUR':
            B.config(text='NUIT')
      else :
            B.config(text='JOUR')

#### Corps  du programme #####
fenetre=Tk()                              
fenetre.title('Bonjour')
B=Button(fenetre,text="JOUR",width=30,command=change)  
B.pack()
fenetre.mainloop()
