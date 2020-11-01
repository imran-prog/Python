# Image Processing In Pillow
import img as img
from PIL import Image, ImageFilter

img = Image.open("4.4 pikachu.jpg")
filter_image = img.convert('L')

filter_image.save("blur.png", "png")
filter_image.show()
