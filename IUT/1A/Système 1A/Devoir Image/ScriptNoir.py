from PIL import Image

i = Image.open("IUT-Orleans.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        pixel = i.getpixel((x,y))
        ecartRVB = (pixel[0]*pixel[0]+pixel[1]*pixel[1]+pixel[2]*pixel[2])>255*255*3/2
        if ecartRVB:
            sortie.putpixel((x,y),(255,255,255))
        else:
            sortie.putpixel((x,y),(0,0,0))

sortie.save("Imageout3.bmp")