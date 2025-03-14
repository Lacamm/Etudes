h=2

for r in range(10): #faire 10 fois la boucle suivante
    n=1
    for t in range(12): #Faire 12 fois n fois h
        a= n*h
        print(n,"x",h," = ", '{:2d}'.format(a))
        n= n+1
    h+=1
    print(" ")
