annee = int(input()) #on donne une année

if annee%4!=0: #on repagrde si c'est un multiple de 4
    print('Ce n\'est pas une année bissextille')
else:
    if annee%100==0: #on regarde si c'est un multiple de 100
        if annee%400==0: #on regarde si c'est un multiple de 400
            print('C\'est une année bissextille')
        else:
            print('Ce n\'est pas une année bissextille')    
    else:
        print('C\'est une année bissextille')


