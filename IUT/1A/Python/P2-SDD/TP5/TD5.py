#!/usr/bin/python3

######################################################################
# Feuille de TD5
# NOM : ALLAIN Lucas
#######################################################################

#######################################################################
print("==========================================")
print("Exercice 4 ")

exemple_catalogue = {'chocolat':5, 'barre de fer':42,
                    'chapeau':25, 'stylo en or': 1050}

cmd1 = {'barre de fer':12, 'chapeau':1}
cmd2 = {'cahier':5}
cmd3 = {'barre de fer':12, 'chapeau':1, 'cahier':5}

def achat(magasin, commande):
    """
    Retourne le prix d'une liste de courses ou
    None si le produit n'est pas présent dans le magasin
    """
    res = 0

    for articles, quantite in commande.items():
        for produits, prix in magasin.items():
            if articles == produits:
                res += prix*quantite
    if res == 0:
        res =None
    
    return res

assert achat(exemple_catalogue, cmd1) == 529
assert achat(exemple_catalogue, cmd2) == None
assert achat(exemple_catalogue, cmd3) == 529

magasin_ville = {'Leclerc':{'chocolat':5, 'vanille':3, 'yaourt':6},
                'Auchan':{'fraise': 4, 'chocolat':3, 'noix de coco':8},
                'Super U':{'fraise':5, 'vanille':6, 'beurre': 3}}


def magasin_produit(magasin, produit):
    """
    Retourne l'ensemble des magasins qui vendent un produit.
    L'ensemble est préférable pour les tests
    """
    ensemble_mag = set()

    for mag, articles in magasin.items():
        for objets in articles.keys():
            if objets == produit:
                ensemble_mag.add(mag)
    return ensemble_mag


assert magasin_produit(magasin_ville, 'chocolat') == {'Leclerc','Auchan'}
assert magasin_produit(magasin_ville, 'bougie') == set()



def moins_cher(magasin, produit):
    """
    Retorune le magasin qui posséde le prduit le moins cher
    """
    def tri(mag):
        return magasin[mag][produit]

    ensemble_mag = magasin_produit(magasin, produit)
    return min(ensemble_mag, key=tri)

assert moins_cher(magasin_ville, 'chocolat') == 'Auchan'


def commande_moins_chere(magasin, commande):
    """
    Retourne le magasin qui est le moins cher pour la commande 
    """

    for produit in commande

    pass

















