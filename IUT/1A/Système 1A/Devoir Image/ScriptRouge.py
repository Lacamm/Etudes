from PIL import Image

i = Image.open("hall-mod_0.bmp")
sortie = i.copy()

for y in range(i.size[1]):
    for x in range(i.size[0]):
        pixel = i.getpixel((x,y))
        rouge = (pixel[0])%2
        if rouge != 0:
                pixel[0]-rouge
        sortie.putpixel((x,y),(pixel))  

sortie.save("Imageout_steg_0.bmp")