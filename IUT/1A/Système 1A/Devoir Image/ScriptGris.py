from PIL import Image

i = Image.open("IUT-Orleans.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        pixel = i.getpixel((x,y))
        gris = (pixel[0]+pixel[1]+pixel[2])//3
        sortie.putpixel((x,y),(gris,gris,gris))

sortie.save("Imageout2.bmp")