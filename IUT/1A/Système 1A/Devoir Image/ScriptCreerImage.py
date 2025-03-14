from PIL import Image

i = Image.open("Imagetest.bmp")
sortie = Image.new(i.mode, i.size)

#Ajoutez cela si voue utilisez une image en mode palette
# de couleurs
#sortie.putpalette(i.getpalette())

sortie.putpalette(i.getdata())
sortie.save("Imageout0.bmp")