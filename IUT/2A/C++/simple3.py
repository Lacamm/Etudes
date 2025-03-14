#!/usr/bin/env python
import svgwrite
from math import *


def apply( points, mat ):
  ((a00, a01, a02),(a10, a11, a12),(a20,a21,a22)) = mat
  output = [None] * len(points)
  for i, point in enumerate(points):
    x,y = point
    a = a00 * x + a01 * y + a02
    b = a10 * x + a11 * y + a12
    output[ i ] = [ a, b ]
  return output
  
def matrot( rot ):
  return (( cos(rot), -sin(rot), 0),( sin(rot), cos(rot), 0), (0, 0, 1))
 
def matscale( coeff ):
  return(( coeff, 0, 0), (0, coeff, 0), (0, 0, 1))
# | coeff  0     | x |x| = | x*coeff |
# | 0      coeff |   |y|   | y*coeff |

def mattrans( dx, dy ):
  return ((1, 0, dx),(0, 1, dy),(0, 0, 1))

def matmul( mat0, mat1 ):
  ((a00, a01, a02), (a10, a11, a12), (a20, a21, a22)) = mat0
  ((b00, b01, b02), (b10, b11, b12), (b20, b21, b22)) = mat1
  return ((a00*b00 + a01*b10 + a02*b20, a00*b01 + a01*b11 + a02*b21, a00*b02 + a01*b12 + a02*b22),\
          (a10*b00 + a11*b10 + a12*b20, a10*b01 + a11*b11 + a12*b21, a10*b02 + a11*b12 + a12*b22),\
          (a20*b00 + a21*b10 + a22*b20, a20*b01 + a21*b11 + a22*b21, a20*b02 + a21*b12 + a22*b22))
# | a00 a01 | x | b00 b01 | = | a00*b00 + a01*b10  a00*b01 + a01 * b11 |
# | a10 a11 |   | b10 b11 |   | a10*b00 + a11*b10  a10*b01 + a11 * b11 |


dessin  = svgwrite.Drawing('exercice_1.svg', size=(800,600))
triangle=[(0,-100),(100,50),(-100,50)]
rectangle=[(0,300),(400,300),(400,600),(0,600)]
carre=[(-100,100),(100,100),(100,-100),(-100,-100)]


dessin.add(dessin.polygon(apply(carre, matmul( matmul( mattrans(200, 200),matrot(pi/4)), matscale(0.2) ) ), fill='#FF0000', stroke="#000000", opacity=1 ))


dessin.save()
