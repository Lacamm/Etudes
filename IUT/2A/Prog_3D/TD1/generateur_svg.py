#!/usr/bin/env python
import svgwrite
dessin  = svgwrite.Drawing('exercice_1-rouge.svg', size=(800,600))
triangle=[(0,0),(400,0),(200,300)]

dessin.add(dessin.polygon(triangle, fill='#FF0000',\
                          stroke="#000000", opacity=0.7 ))
dessin.save()