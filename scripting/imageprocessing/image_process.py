from PIL import Image, ImageFilter

img = Image.open('pika.png')
#filtered_img = img.filter(ImageFilter.BLUR)
filtered_img = img.convert('L')
filtered_img.save("blur.png")

img.show()





