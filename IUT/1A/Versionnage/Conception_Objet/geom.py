class point(object):

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        return "<point %s,%s>" % (self._x, self._y)

    def __eq__(self, other):
        return self._x == other._x and self._y == other._y


    def getx(self):
        return self._x

    def gety(self):
        return self._y


class rectangle(object):

    def __init__(self, x, y, width, height):

        self._ptBG = point(x,y)
        self._width = width
        self._height = height
    
    def getPtBG(self):
        return self._ptBG
        
    def getHeight(self):
        return self._height

    def getWidth(self):
        return self._width