from box import *
from things import *

def test_box_create():
    b = Box()

def test_box_add():
    b = Box()
    b.add("truc1")
    b.add("truc2")

def test_truc_in_box():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    assert "truc1" in b
    assert "truc3" not in b

def test_box_remove():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    b.remove("truc1")

    assert "truc1" not in b
    assert "truc2" in b

    try:
        b.remove("truc3")
        assert False
    except ValueError:
        pass
    
def test_open_box():
    b = Box()

    b.Open(True)
    assert b.is_open()
    b.Close(False)
    assert not b.is_open()

def test_objet_boite():
    b = Box()
    b.add("truc1")
    b.add("truc2")

    b.Close(False)
    assert b.actionLook() == "La boîte est fermée"

    b.Open(True)
    assert b.actionLook() == "La boîte contient:'truc1, truc2'"

def test_capacity():
    b = Box()
    b.setCapacity(5)
    assert b.capacity() == 5

def test_capacite_restante():

    b = Box()
    b.setCapacity(5)
    t = Thing(5)
    assert b.has_room_for(t)

    b = Box()
    b.setCapacity(5)
    t = Thing(6)
    assert not  b.has_room_for(t)

    b = Box()
    t = Thing(1000000000000)
    assert  b.has_room_for(t)
