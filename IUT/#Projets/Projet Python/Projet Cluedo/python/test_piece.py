import piece

piece1 = (1,[("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)],[5,8,2,35,4],[4,[3,5]])
piece11 = (1,[("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)],[5,8,2,35,4],[4,[3,5]])
piece12 = (1,[("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)],[5,8,2,35,4],[4,[3,5]])
piece13 = (1,[("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)],[5,8,2,35,4],[4,[3,5]])
piece14 = (1,[("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)],[5,8,2,35,4],[4,[3,5]])

piece2 = (5,[("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)],[1,2,3,4,5,6],[None,[None,None]])
piece21 = (5,[("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)],[1,2,3,4,5,6],[None,[None,None]])
piece22 = (5,[("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)],[1,2,3,4,5,6],[None,[None,None]])
piece23 = (5,[("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)],[1,2,3,4,5,6],[None,[None,None]])
piece24 = (5,[("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)],[1,2,3,4,5,6],[None,[None,None]])


assert piece.getNumPiece(piece1) == 1
assert piece.getListeEntrees(piece1) == [("NORD",1,2),("SUD",5,7),("EST",4,6),("OUEST",3,8)]
assert piece.getContenu(piece1) == [5,8,2,35,4]
assert piece.getPassage(piece1) == 4
assert piece.getEntreesDirection(piece1,("NORD")) == [("NORD",1,2)]
piece.setPassage(piece11,None, None,None)
assert piece.getPassage(piece11) == None
piece.addEntree(piece12,("NORD",4,4))
assert piece.getEntreesDirection(piece12,("NORD")) == [("NORD",1,2),("NORD",4,4)]
piece.addJoueur(piece13, 99)
assert piece.getContenu(piece13) == [5,8,2,35,4,99]
piece.enleverJoueur(piece14, 4)
assert piece.getContenu(piece14) == [5,8,2,35]
assert piece.estEntree(piece1,5,7)
assert not piece.estEntree(piece1,4,8)
assert piece.estPassage(piece1,3,5) == 4
assert piece.estPassage(piece1,3,6) == 0


assert piece.getNumPiece(piece2) == 5
assert piece.getListeEntrees(piece2) == [("NORD",5,3),("SUD",3,9),("EST",5,5),("OUEST",7,9)]
assert piece.getContenu(piece2) == [1,2,3,4,5,6]
assert piece.getPassage(piece2) == None
assert piece.getEntreesDirection(piece2,"SUD") == [("SUD",3,9)]
piece.setPassage(piece21, 8,1,2)
assert piece.getPassage(piece21) == 8
piece.addEntree(piece22,("EST",4,9))
assert piece.getEntreesDirection(piece22,("EST")) == [("EST",5,5),("EST",4,9)]
piece.addJoueur(piece23,77)
assert piece.getContenu(piece23) == [1,2,3,4,5,6,77]
piece.enleverJoueur(piece24,4)
assert piece.getContenu(piece24) == [1,2,3,5,6]
assert piece.estEntree(piece2,7,9)
assert not piece.estEntree(piece2,5,8)
assert piece.estPassage(piece2,None,None) == None
assert piece.estPassage(piece2,2,8) == 0