from geom import *

def test_proprietes():
    rec = rectangle(1,2,4,9)

    assert rec.getPtBG() == point(1,2)
    assert rec.getWidth() == 4
    assert rec.getHeight() == 9