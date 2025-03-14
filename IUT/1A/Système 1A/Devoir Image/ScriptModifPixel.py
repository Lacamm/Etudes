from PIL import Image

i = Image.open("Image0.bmp")
sortie = i.copy()
sortie.putpixel((1,2),(0,0,255))
sortie.save("Imageout.bmp")