######################################################################
# Devoir Image
# NOM : DOLPHIN Nicolas 1A31
#######################################################################


######################################################################
# Importation
######################################################################
from PIL import Image


#######################################################################
print("==========================================")
print("Question B.1")


def Transposition(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de transpose une image
    :param Image_Entree: image a transpose (doit exister)
    :param Image_Sortie: image transpose (pas obliger d'exister)
    '''
    image= Image.open(Image_Entree)
    sortie = image.copy()
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
            pixel = image.getpixel((x, y))
            sortie.putpixel((y, x), pixel)
    sortie.save(Image_Sortie)

Transposition("images/Imagetest.bmp", "images/Imageout0.bmp")

#######################################################################
print("==========================================")
print("Question B.2")

def inversion_miroir(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de faire une iversion miroir
    :param Image_Entree: image a inverser (doit exister)
    :param Image_Sortie: image inverser (pas obliger d'exister)
    '''
    image=Image.open(Image_Entree)
    sortie=image.copy()
    milieu=sortie.size[0]//2
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
            pixel=image.getpixel((x,y))
            if x == 0:
                sortie.putpixel(((x + sortie.size[0] - 1), y), pixel)
            elif x < milieu:
                z=milieu-x
                sortie.putpixel(((milieu+z),y),pixel)
            else:
                z=x-milieu
                sortie.putpixel(((milieu-z),y),pixel)
    sortie.save(Image_Sortie)

inversion_miroir("images/hall-mod_0.bmp","images/Imageout1.bmp")

#######################################################################
print("==========================================")
print("Question B.3")

def passage_niveau_gris(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de passer un eimage au niveaux gris
    :param Image_Entree: image a mettre au nivaux gris (doit exister)
    :param Image_Sortie: image paseer au nuveaux gris spose (pas obliger d'exister)
    '''
    image = Image.open(Image_Entree)
    sortie = image.copy()
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
            pixel = image.getpixel((x,y))
            Gris = (pixel[0]+pixel[1]+pixel[2])//3
            sortie.putpixel((x, y), (Gris, Gris, Gris))
    sortie.save(Image_Sortie)

passage_niveau_gris("images/IUT-Orleans.bmp","images/Imageout2.bmp")

#######################################################################
print("==========================================")
print("Question B.4")

def passage_en_noir_et_blanc(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de passer une image en noir et blanc
    :param Image_Entree: image a mettre en noir et blanc  (doit exister)
    :param Image_Sortie: image e noir et blanc  (pas obliger d'exister)
    '''
    image=Image.open(Image_Entree)
    sortie=image.copy()
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
           pixel=image.getpixel((x,y))
           distance=(pixel[2]**2+pixel[1]**2+pixel[0]**2)>255*255*3/2
           if distance :
               sortie.putpixel((x,y),(255,255,255))
           else:
               sortie.putpixel((x,y),(0,0,0))
    sortie.save(Image_Sortie)

passage_en_noir_et_blanc("images/IUT-Orleans.bmp","images/Imageout3.bmp")

#######################################################################
print("==========================================")
print("Question B.5")

def mettre_rouge_val_paire(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de mettre toutes les valeurs rouges de chaque pixel à une valeur paire
    :param Image_Entree: image a changer  (doit exister)
    :param Image_Sortie: image changee (pas obliger d'exister)
    '''
    image=Image.open(Image_Entree)
    sortie=image.copy()
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
            pixel=image.getpixel((x,y))
            a=pixel[0]%2
            if a != 0: pixel[0]-a
            sortie.putpixel((x,y),pixel)
    sortie.save(Image_Sortie)


mettre_rouge_val_paire("images/hall-mod_0.bmp","images/Imageout_steg_0.bmp")
# Je ne vois aucune grosse diffence

def cacher(i,b):
    return i-(i%2)+b


def trouver(i):
    return i % 2


def Stéganographie(Image_Entree,Image_Cacher,Image_Sortie):
    '''
    Cette fonction a pour objectif de dissimuler une image dans une autre
    :param Image_Entree: image d'origine
    :param Image_Cacher: image a cacher
    :param Image_Sortie: image avec l'image dissimuler
    '''
    image = Image.open(Image_Entree)
    image_cacher = Image.open(Image_Cacher)
    sortie = image.copy()
    for x in range(image_cacher.size[0]):
        for y in range(image_cacher.size[1]):
            pixel_image1 = image.getpixel((x, y))
            pixel_image2 = image_cacher.getpixel((x, y))
            if pixel_image2[0]==255:
                sortie.putpixel((x, y), (cacher(pixel_image1[0], 0), pixel_image1[1], pixel_image1[2]))
    sortie.save(Image_Sortie)

Stéganographie("images/Imageout_steg_0.bmp","images/Imageout3.bmp","images/Imageout_steg_1.bmp")


def extraire_image_cacher(Image_Entree,Image_Sortie):
    '''
    Cette fonction a pour objectif de trouver une image cacher par Stéganographie dans une autre
    :param Image_Entree: image a etudie  (doit exister)
    :param Image_Sortie: image cache (pas obliger d'exister)
    '''
    image=Image.open(Image_Entree)
    sortie=image.copy()
    for x in range(sortie.size[0]):
        for y in range(sortie.size[1]):
            pixel=image.getpixel((x,y))
            if trouver(pixel[0])!=0:
                sortie.putpixel((x, y), (255, 255, 255))
            else:
                sortie.putpixel((x, y), (0, 0, 0))
    sortie.save(Image_Sortie)

extraire_image_cacher("images/Imageout_steg_1.bmp","images/Imageout3bis.bmp")