from geom import point

def test_creation():
    p = point(22,7)
    p2 = point(3,4)
    assert 22 == p.getx()
    assert 7 == p.gety()
    assert 3 == p2.getx()
    assert 4 == p2.gety()

def test_equality():
    p1 = point(1,3)
    p2 = point(1,3)
    p3 = point(2,5)
    assert p1 == p1
    assert p1 == p2
    assert p2 == p1
    assert p1 != p3