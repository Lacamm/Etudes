def bombes(coordonnees):
    caracteristique_BOM =[20]
    caracteristique_BOM = caracteristique_BOM + coordonnees
    return caracteristique_BOM


global caracteristique_BOM
caracteristique_BOM = []

coordonnees = [5, 12]
print(bombes(coordonnees))
