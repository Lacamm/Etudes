def tirerUnTrait():
    print("-------------------------")
    print()
    print()
    return ()

def annoncerUnVol(destination, horaire):
    print("Le vol en direction de", end= " ")
    print(destination, end=" ")
    print("décollera à", end=" ")
    print(horaire)
    print(tirerUnTrait())
    return (destination, horaire)

def afficher():
    destination = " "
    horaire = " "
    destination = input("Destination? ")
    horaire = input("Horaire? ")
    annoncerUnVol(destination, horaire)
    return ()

destination = " "
horaire = " "
afficher()

while len(destination) != 0:
    afficher()
    if len(destination) == 0:
        print("Fin des voyages")
        break
