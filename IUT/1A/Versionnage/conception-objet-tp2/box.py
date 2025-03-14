class Box(object):
    
    def __init__(self,ouverture = False, capacite = None):
        self._contents = []
        self._ouverture = ouverture
        self._capacite = capacite

    def __contains__(self, machin):
        return machin in self._contents

    def add(self, truc):
        self._contents.append(truc)
    
    def remove(self,truc):
        self._contents.remove(truc)
    
    def is_open(self):
        return self._ouverture

    def Open(self,ouverture):
        self._ouverture = ouverture

    def Close(self,ouverture):
        self._ouverture = ouverture

    def actionLook(self):
        res = ""
        if self.is_open():
            objets = repr(", ".join(self._contents))
            res = "La boîte contient:"+ objets 
        else:
            res = "La boîte est fermée"
        return res
    
    def setCapacity(self,capacite):
        self._capacite = capacite

    def capacity(self):
        return self._capacite

    def has_room_for(self,truc):
        if self._capacite == None:
            return True
        elif self._capacite >= truc.taille:
            return True
        else:
            return False