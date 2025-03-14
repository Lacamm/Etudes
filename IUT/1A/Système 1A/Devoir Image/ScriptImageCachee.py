from PIL import Image


def cacher(i,b):
    return i-(i%2)+b


i = Image.open("Imageout_steg_0.bmp")
img = Image.open("Imageout3.bmp")
sortie = i.copy()

for y in range(img.size[1]):
    for x in range(img.size[0]):
        pixel_img1 = i.getpixel((x,y))
        pixel_img2 = img.getpixel((x,y))
        if pixel_img2[0] == 255:
            sortie.putpixel((x,y),(cacher(pixel_img1[0],0),pixel_img1[1], pixel_img1[2]))
sortie.save("Imageout_steg_1.bmp")



