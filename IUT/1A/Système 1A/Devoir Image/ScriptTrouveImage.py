from PIL import Image


def trouver(i):
    return i%2


image=Image.open("Imageout_steg_1.bmp")
sortie=image.copy()
for x in range(sortie.size[0]):
    for y in range(sortie.size[1]):
        pixel=image.getpixel((x,y))
        if trouver(pixel[0])==0:
            sortie.putpixel((x, y), (255, 255, 255))
        else:
            sortie.putpixel((x, y), (0, 0, 0))
sortie.save("Imageout_steg_3.bmp")
