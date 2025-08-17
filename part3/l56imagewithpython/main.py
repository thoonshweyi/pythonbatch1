from PIL import Image

img = Image.open("./assets/cutedog.jpg")
print(img) # <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x427 at 0x17E3D2670B0>

print(img.format) # JPEG
print(img.size) # (640, 427)
print(img.mode) # RGB





# pip3 install openpyxl