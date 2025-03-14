class Person(object):
    def __init__(self, firstname=None, lastname=None):
        self.firstname = firstname
        self.lastname  = lastname

    @staticmethod 
    def from_data(data):
        f = data.get("firstname", None)
        l  = data.get("lasname"  , None)
        return Person(firstname=f, lastname=l)

from exeYAML import newDico

newPersonne = Person.from_data(newDico)

print(newPersonne.firstname)
print(newPersonne.lastname)