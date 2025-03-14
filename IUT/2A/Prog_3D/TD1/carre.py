#!/usr/bin/env python
import svgwrite
dessin  = svgwrite.Drawing('3d.svg', size=(1000,1000))
carre=[(-100,-100),(100,-100),(100,100),(-100,100)]


trans=(200,300)

#dessin.add(dessin.polygon(carre, fill='#008000',\
#                          stroke="#000000", opacity=0.7 ))


def translater(polygone, vecteur):
    def translater_sommet(sommet):
        x,y=sommet
        dx,dy=vecteur
        return (x+dx, y+dy)
    return [translater_sommet(sommet) for sommet in polygone]

#dessin.add(dessin.polygon(translater(carre,(200,200)), fill='#000800',\
#                          stroke="#000000", opacity=0.7 ))


from math import sin, cos, pi

def rotation(polygone, angle):
    def rotation_sommet(sommet):
        x, y = sommet

        return x*cos(angle) - y*sin(angle), x*sin(angle) + y*cos(angle)
    return [rotation_sommet(sommet) for sommet in polygone] 

carre_tourne = rotation(carre, pi/12)
carre_tourne_translate = translater(carre_tourne,(200,300))

#dessin.add(dessin.polygon(carre_tourne_translate, fill='#0000FF',\
#                          stroke="#000000", opacity=0.7 ))

def prodMatVect(Mat, Vect ):
    x, y = Vect
    ( (a11,a12), (a21, a22) ) = Mat

    x2 = a11 * x + a12 * y
    y2 = a21 * x + a22 * y

    return (x2,y2)

def Matrotation(angle):
    return ((cos(angle), -sin(angle)),(sin(angle), cos(angle)))
    # return ((0.5,0),(0,0.5))  # réduit

def tourner(polygone,angle):
    M = Matrotation(angle)
    return [prodMatVect(M, sommet) for sommet in polygone]

carre_tourne = tourner(carre, pi/12)
carre_tourne_translate = translater(carre_tourne,(200,300))

#dessin.add(dessin.polygon(carre_tourne_translate, fill='#0000FF',\
#                          stroke="#000000", opacity=0.7 ))


############# Dilatation #############

def MatDilatation(coeff):
    return (coeff, 0), (0,coeff)

def dilater(polygone, coeff):
    M = MatDilatation(coeff)
    return [prodMatVect(M, sommet) for sommet in polygone]


for i in range(4):
    carre_petit = dilater(carre, 0.5**i)
    #carre_petit_translater = translater(carre_petit, (150*i, 150))
    #carre_petit_translater = translater(carre_petit, (200,300))
    #dessin.add(dessin.polygon((carre_petit_translater),fill='#0000FF', stroke='#000000', opacity=0.7))


############# Modélisation #############

#matrice_dilatation = MatDilatation(0.75)
#matrice_rotation = Matrotation(pi/12)

def prodMatMat(MatA, MatB):
    ( (a11,a12), (a21,a22) ) = MatA
    ( (B11,B12), (B21,B22) ) = MatB
    return ( (a11*B11+a12* B21 , a11*B12+a12*B22 ), (  a21*B11+a22*B21 , a21*B12+a22*B22  ) )


for i in range(10):
    MatModelisation=prodMatMat(Matrotation((pi/12)*i),MatDilatation(0.75))
    #carre_out = translater([prodMatVect(MatModelisation,sommet) for sommet in carre], (75*i,150))

    #MatModelisation=prodMatMat(Matrotation(-(pi/12)*i),MatDilatation(0.75/(i+1)))
    #carre_out = translater([prodMatVect(MatModelisation,sommet) for sommet in carre], (50*i +150,150))

    #dessin.add(dessin.polygon((carre_out),fill='#FF0000', stroke='#000000', opacity=0.7))


############# Limiter calculs #############

aux=100
points=[(aux, aux),(-aux, aux),(-aux, -aux),(aux, -aux)]
triangles=[0,1,2,0,2,3]

#point2 = translater( dilater(rotation(points, pi/2), 1.5),trans)

point2 = translater( dilater(points, 1.5),(300,300))

i=0
#dessin.add(dessin.polygon((point2[triangles[3*i]],point2[triangles[3*i+1]],point2[triangles[3*i+2]]), fill='blue',  opacity=0.5,stroke='black'))
i=1
#dessin.add(dessin.polygon((point2[triangles[3*i]],point2[triangles[3*i+1]],point2[triangles[3*i+2]]), fill='blue',  opacity=0.5,stroke='black'))


def compose(points,triangles):
  liste_point=[]
  colors=("blue","red","green","purple","yellow","white","coral","darkblue")
  for i in range(0,len(triangles)//3):
      print(triangles[3*i],triangles[3*i+1],triangles[3*i+2])
      dessin.add(dessin.polygon((points[triangles[3*i]],points[triangles[3*i+1]],points[triangles[3*i+2]]), fill=colors[(i%(len(colors)*2))//2],  opacity=0.5,stroke='black'))

#compose(point2, triangles)

############# Chat #############

pointsChat=[(-100,-70),(-100,0),(-50,0),(0,50),(100,0),(0,-30),(50,0),(100,-70)]
trianglesChat=[0,1,2, 1,3,4, 2,5,6, 6,4,7]

pointChatT = rotation(pointsChat, -pi/12)

# for n in range(5):
#     pointChat2 = translater(dilater(rotation(pointChatT, pi/3*n), 0.75/(n+1)),(75*n+150,300))

#     i=0
#     dessin.add(dessin.polygon((pointChat2[trianglesChat[3*i]],pointChat2[trianglesChat[3*i+1]],pointChat2[trianglesChat[3*i+2]]), 
#                                 fill='blue',  opacity=0.5,stroke='black'))
#     i=1
#     dessin.add(dessin.polygon((pointChat2[trianglesChat[3*i]],pointChat2[trianglesChat[3*i+1]],pointChat2[trianglesChat[3*i+2]]), 
#                                 fill='purple',  opacity=0.5,stroke='black'))
#     i=2
#     dessin.add(dessin.polygon((pointChat2[trianglesChat[3*i]],pointChat2[trianglesChat[3*i+1]],pointChat2[trianglesChat[3*i+2]]), 
#                                 fill='red',  opacity=0.5,stroke='black'))
#     i=3
#     dessin.add(dessin.polygon((pointChat2[trianglesChat[3*i]],pointChat2[trianglesChat[3*i+1]],pointChat2[trianglesChat[3*i+2]]), 
#                                 fill='green',  opacity=0.5,stroke='black'))


############# 3D #############

aux=100
points_3d=[[-aux, -aux, aux], #point 0 (face devant)
        [-aux, aux, aux],#point 1   (face devant)
        [aux, aux, aux],#point 2    (face devant)
        [aux, -aux, aux],#point 3   (face devant)
        [-aux, -aux, -aux],#point 4 (face arrière)
        [-aux,aux,-aux],#point 5    (face arrière)
        [aux,aux,-aux],#point 6     (face arrière)
        [aux,-aux,-aux]]#point 7     (face arrière)    

cube=[0,1,2,    #triangle 1 face 1 (devant)
    0,2,3,      #triangle 2 face 1
    4,5,6,      #triangle 1 face 2 (arriere)
    4,7,6,      #triangle 2 face 2
    0,4,3,      #triangle 1 face 3 (dessus)
    4,7,3,      #traingle 2 face 3
    1,0,4,      #triangle 1 face 4 (coté gauche)
    1,5,4,      #traingle 2 face 4
    2,3,7,      #trianlge 1 face 5 (coté droit)
    2,6,7,      #triangle 2 face 5 
    1,2,6,      #triangle 1 face 6 (dessous)
    1,5,6]      #triangle 2 face 6

trans3d=(200,200,200)

def projection(point3d):
    return(point3d[0],point3d[1])

# points_proj = [ projection(sommet) for sommet in points_3d ]
# compose(points_proj,cube)


def translater_3d(point, direction):
    x, y, z = point
    dx, dy, dz = direction
    return (x + dx, y + dy, z + dz)

points_3dt = []

# for i in range(8):
#     points_3dt.append(translater_3d(points_3d[i],trans3d))

# points_proj = [ projection(sommet) for sommet in points_3dt ]
# compose(points_proj,cube)


def prodMatVect3D(Mat, Vect ):
    x, y,z = Vect
    ( (a11,a12,a13), (a21, a22,a23), (a31, a32,a33) ) = Mat

    x2 = a11 * x + a12 * y+ a13 * z
    y2 = a21 * x + a22 * y+ a23 * z
    z2 = a31 * x + a32 * y+ a33 * z

    return (x2,y2,z2)

def prodMatMat3D(MatA, MatB ):

    ( (a11,a12,a13),
    (a21, a22,a23),
    (a31, a32,a33) )  = MatA

    ( (b11,b12,b13),
    (b21, b22,b23),
    (b31, b32,b33) )  = MatB

    return ( (a11*b11+a12* b21+a13*b31 , a11*b12+a12* b22+a13*b32,a11*b13+a12* b23+a13*b33  ),
     (  a21*b11+a22* b21+ a23*b31, a21*b12+a22* b22 +a23*b32,  a21*b13+a22* b23+a23*b33),
     (  a31*b11+a32* b21+ a33*b31, a31*b12+a32* b22 +a33*b32,  a31*b13+a32* b23+a33*b33))

def Matdilatation3D(coefDilatation):
         return ((coefDilatation, 0, 0),
                 (0, coefDilatation, 0),
                 (0, 0, coefDilatation))


def dilatation3D(sommet,coeff):
    M = Matdilatation3D(coeff)
    return prodMatVect3D(M,sommet)

#compose([projection(dilatation3D(sommet,2)) for sommet in points_3dt],cube)

def Matrotation3DX(angle):
     return (
            (1, 0, 0,),
            (0, cos(angle), -sin(angle)),
            (0, sin(angle),  cos(angle)))

def Matrotation3DY(angle):
     return (
            (cos(angle), 0,sin(angle)),
            (0,1,0,),
            (-sin(angle),0, cos(angle)))

def Matrotation3DZ(angle):
     return (
            (cos(angle), -sin(angle), 0),
            (sin(angle),  cos(angle), 0),
            (0, 0, 1))


def rotation3DX(sommet,angle):
    M = Matrotation3DX(angle)
    return prodMatVect3D(M,sommet)

def rotation3DY(sommet,angle):
    M = Matrotation3DY(angle)
    return prodMatVect3D(M,sommet)

def rotation3DZ(sommet,angle):
    M = Matrotation3DZ(angle)
    return prodMatVect3D(M,sommet)


# MatRota3DX = [rotation3DX(sommet,pi/24) for sommet in points_3dt]

# MatRota3DY = [rotation3DY(sommet,pi/6) for sommet in MatRota3DX]

# compose([projection(rotation3DZ(sommet,pi/12)) for sommet in MatRota3DY],cube)


listPointTrans = []

points_cube_f = points_3d

for i in range(10):

    listPointX = [rotation3DX(sommet,(pi/24)*i) for sommet in points_cube_f]
    #print(listPointX)

    listPointY = [rotation3DY(sommet,(pi/6)*i) for sommet in listPointX]
    #print(listPointY)

    listPointZ = [rotation3DZ(sommet,(pi/12)*i) for sommet in listPointY]
    #print(listPointZ)

    listPointDila = [dilatation3D(sommet,0.5/(i+1)) for sommet in listPointZ]
    #print(listPointDila)

    listPointTrans = [translater_3d(sommet, (200*i,200,200)) for sommet in listPointDila]
    #print(listPointTrans)


    compose([ projection(sommet) for sommet in listPointTrans ],cube)

dessin.save()
