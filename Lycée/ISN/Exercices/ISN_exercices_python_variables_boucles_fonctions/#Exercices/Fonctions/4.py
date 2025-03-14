def inverse(ch):
    ch1 = " "
    for n in range(len(ch)):
        ch1 = ch1 + ch[len(ch)-n-1] #On prend le dernier terme de la châine puis on désincrément
    return ch1
    
##################
#prog
##################

#On définit le type de stockage
ch = " "
ch1 = " "
ch = input("Chaîne de caractères: ")
print(inverse(ch))
