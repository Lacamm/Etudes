import case

case1 = [None,None]
case11 = [None,None]
case2 = [0,4]
case21 = [0,4]
case3 = [-4,None]
case31 = [-4,None]

assert case.getCategorie(case1) == None
assert case.getContenu(case1) == None
assert not case.estLibre(case1)
assert case.estDepart(case1) == 0
case.setContenu(case1,0)
assert case.getContenu(case1) == 0
case.setCategorie(case11,-1)
assert case.getCategorie(case11) == -1


assert case.getCategorie(case2) == 0
assert case.getContenu(case2) == 4
assert not case.estLibre(case2)
assert case.estDepart(case2) == 0
case.setContenu(case2,9)
assert case.getContenu(case2) == 9
case.setCategorie(case21,0)
assert case.getCategorie(case21) == 0


assert case.getCategorie(case3) == -4
assert case.getContenu(case3) == None
assert case.estLibre(case3)
assert case.estDepart(case3) == 4
case.setContenu(case3,4)
assert case.getContenu(case3) == 4
case.setCategorie(case31,0)
assert case.getCategorie(case31) == 0