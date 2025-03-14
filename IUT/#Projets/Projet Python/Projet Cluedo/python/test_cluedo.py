import cluedo
import jeucarte

testlistejoueur=[(1,'MAXBUTTY'),(2,'MAMADOU'),(3,'JESAISPAS'),(4,'BONJOUR'),(5,'ADEMAIN')]
testlistenumjoueur=[1,2,3,4,5]
testjeucarte=[(1,'salle1',2,'une salle',True),(2,'salle2',2,'une autre salle',True),(1,'prof1',0,'un prof',True),(2,'prof2',0,'une prof',False),(1,'mat1',1,'une matiere',True),(2,'mat2',1,'une AUTRE matiere',True)]

listeJ = [[1,'MAXBUTTY',True,False,[],None],[2,'MAMADOU',False,False,[],None],[3,'JESAISPAS',True,False,[],None],[4,'BONJOUR',False,False,[],None],[5,'ADEMAIN',False,False,[],None]]

piece1=[1,[(0,1,2)],[],[None,[None,None]]]
piece2=[2,[(1,2,1)],[],[3,[2,1]]]
piece3=[3,[(2,0,2)],[],[None,[None,None]]]

liste_piece = [piece1,piece2,piece3]
listeDest = [(1,1),(1,2)]

cluedo1 = {'jeuCarte': [(1,'Salle à manger',3,'mangeeer',True),(2,'SDD',2,'SE PENDRE',True),(3,'i23',3,'TRAVAILLLER',True)], 'plateau': [[[0,0],[0,0]],[(1,[(1,2),(2,2)],[1,4,5,2],[None,[None,None]],[(2,[(0,2),(1,0)],[3],[None,[None,None]])])]], 'listeJoueurs': listeJ,
            'solution': (1,3,2), 'joueurCourant': listeJ[0], 'numTour': 1,'pieces': liste_piece}


assert cluedo.getJoueurCourant(cluedo1) == [1,'MAXBUTTY',True,False,[],None]
assert cluedo.getIndiceJoueurCourant(cluedo1) == 0
assert cluedo.getSolution(cluedo1) == (1,3,2)
assert cluedo.getNbJoueurs(cluedo1) == 5
assert cluedo.getNbJoueursActifs(cluedo1) == 5
assert cluedo.getJoueurPrincipal(cluedo1) == [1,'MAXBUTTY',True,False,[],None]
assert cluedo.getNumTour(cluedo1) == 1
assert cluedo.getPlateau(cluedo1) == [[[0,0],[0,0]],[(1,[(1,2),(2,2)],[1,4,5,2],[None,[None,None]],[(2,[(0,2),(1,0)],[3],[None,[None,None]])])]]
assert cluedo.getJeuCartes(cluedo1) == [(1,'Salle à manger',3,'mangeeer',True),(2,'SDD',2,'SE PENDRE',True),(3,'i23',3,'TRAVAILLLER',True)]
assert cluedo.getListeJoueurs(cluedo1) == [[1,'MAXBUTTY',True,False,[],None],[2,'MAMADOU',False,False,[],None],[3,'JESAISPAS',True,False,[],None],[4,'BONJOUR',False,False,[],None],[5,'ADEMAIN',False,False,[],None]]
assert cluedo.getNumPieceHypothese(cluedo1) == 2
cluedo.incNumTour(cluedo1)
assert cluedo.getNumTour(cluedo1) == 2
cluedo.elimineJoueurCourant(cluedo1)
assert cluedo.getNbJoueursActifs(cluedo1)
assert cluedo.distancePieces(cluedo1,liste_piece,listeDest) =={1: (0, 1, 2), 2: (1, 1, 1), 3: (1, 1, 2)}


"""
assert cluedo.choixPieceOrdinateur(cluedo1,distances)
assert cluedo.reponsePassageOrdinateur(cluedo1,numP)
assert cluedo.passageSecretJoueurCourant(cluedo1)
assert cluedo.choixProfMatOrdinateur(cluedo1,numPiece)
assert cluedo.choixSolutionOrdinateur(cluedo1)
assert cluedo.demanderJoueurOrdinateur(cluedo1,joueurInterroge,hypothese)
assert cluedo.jouerDe(cluedo1)
assert cluedo.deplacerJoueurCourant(cluedo,lig,col)

assert cluedo.joueurPrincipal(1)
assert cluedo.distribuerCartes(cluedo1)
"""