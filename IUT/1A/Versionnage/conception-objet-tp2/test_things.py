from things import *

def test_things_create():
    t = Thing(3)

def test_volume():
    t = Thing(4)
    assert t.volume() == 4