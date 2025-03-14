import plateau
import case

listeDeliste=[[[-1,None],[2,None],[0,1],[3,None]],[[0,None],[2,None],[0,None],[3,2]],[[4,None],[0,None],[5,3],[0,None]]]
listeDeliste1=[[[-1,None],[2,None],[0,1],[3,None]],[[0,None],[2,None],[0,None],[3,2]],[[4,None],[0,None],[5,3],[0,None]]]

piece1=[1,[(0,1,2)],[],[None,[None,None]]]
piece2=[2,[(1,2,1)],[],[3,[2,1]]]
piece3=[3,[(2,0,2)],[],[None,[None,None]]]

piece11=[1,[(0,1,2)],[],[None,[None,None]]]
piece21=[2,[(1,2,1)],[],[3,[2,1]]]
piece31=[3,[(2,0,2)],[],[None,[None,None]]]
piece41=[6,[(3,5,0)],[],[4,[1,1]]]

plateau1 = [listeDeliste,[piece1,piece2,piece3]]
plateau11 = [listeDeliste,[piece1,piece2,piece3]]
plateau12 = [listeDeliste,[piece1,piece2,piece3]]
plateau13 = [listeDeliste,[piece1,piece2,piece3]]
plateau14 = [listeDeliste,[piece1,piece2,piece3]]
plateau15 = [listeDeliste1,[piece11,piece21,piece31,piece41]]

assert plateau.getNbLignesP(plateau1) == 3
assert plateau.getNbColonnesP(plateau1) == 4
assert plateau.getCase(plateau1,1,3) == [3,2]
assert plateau.getPieces(plateau1) == [piece1,piece2,piece3] 
assert plateau.getCategorieP(plateau1,0,1) == 2
assert plateau.getContenuP(plateau1,0,1) == None
assert plateau.getPassageSecret(plateau1,2,1) == 2
plateau.setCase(plateau1,1,3,0)
assert plateau.getCase(plateau1,1,3) == [0,None]
plateau.setPieces(plateau11,piece3)
assert plateau.getPieces(plateau11) == piece3
assert plateau.enleverPion(plateau12,0,2) == 1
plateau.mettrePion(plateau13,0,0,1)
assert plateau.getContenuP(plateau13,0,0) == 1
plateau.poserPionCaseDepart(plateau14,[1,2,3])
assert case.estDepart(plateau.getCase(plateau14,0,0)) == 1
assert plateau.posJoueur(plateau15,2) == (1,3)
assert plateau.estEntreePiece(plateau15,1,2)
assert not plateau.estPassageSecret(plateau15,1,2)
assert plateau.passageNord(plateau1,1,2)
assert not plateau.passageNord(plateau1,1,1)
assert plateau.passageSud(plateau15,0,2)
assert not plateau.passageSud(plateau15,0,1)
assert plateau.passageEst(plateau15,2,2)
assert not plateau.passageEst(plateau15,2,1)
assert plateau.passageOuest(plateau15,2,0)
assert not plateau.passageOuest(plateau15,1,0)

print(plateau.accessiblesJoueur(plateau1,1,2))

"""
assert plateau.casesAccessibles(plateau1,listeDepart,distance) == 
assert plateau.distancePieces(plateau1,lig,col) == 
assert plateau.accessiblesJoueur(plateau1,numJoueur,distance) ==
"""