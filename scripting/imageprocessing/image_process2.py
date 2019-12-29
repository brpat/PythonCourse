from PIL import Image, ImageFilter

img = Image.open('wallpaper.jpg')
#filtered_img = img.filter(ImageFilter.BLUR)
comp_img = img.resize((400, 300))
comp_img.save("compressed.png", "png")

img.show()





