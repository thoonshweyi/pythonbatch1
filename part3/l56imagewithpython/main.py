from PIL import Image

img = Image.open("./assets/cutedog.jpg")
print(img) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x427 at 0x17E3D2670B0>

print(img.format) # JPEG
print(img.size) # (640, 427)
print(img.mode) # RGB

# filteredimg = img.filter(ImageFilter.BLUR)
# filteredimg.save("newblurimg.png","png")

# filteredimg = img.filter(ImageFilter.SMOOTH)
# filteredimg.save("newsmoothimg.png","png")


# filteredimg = img.filter(ImageFilter.SMOOTH)
# filteredimg.save("newsharpenimg.png","png")

# ------------------------------------------

#=> convert
filteredimg = img.convert("L")
filteredimg.save("newconvertimg.png","png") # black white

# => ratate
filteredimg = img.convert("L")
rotatedimg = filteredimg.rotate(-90)
rotatedimg.save("newrotateimg.png","png")

# => resize
print(img.size)
resizedimg = img.resize((300,300))
print(resizedimg.size)
resizedimg.save("newresizeig.png","png")


# => thumbnail(), note: must be save with img
# print(img.size)
# resizedimg = img.thumbnail((300,300)) 
# print(img.size) # (300, 200)
# img.save("newthumbnail.png","png")


# => crop (left, upper, right, lower)

cpsize = (100,0,300,408)
print(img.size) # (640, 427)
filteredimg = img.crop(cpsize) # one parameter
filteredimg.save("newcropimg.png","png")
print(filteredimg.size) # (200, 408)








# pip3 install openpyxl