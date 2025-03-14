from PIL import Image

i = Image.open("Image3.bmp")
sortie = i.copy()
sortie.save("Imageout.bmp")