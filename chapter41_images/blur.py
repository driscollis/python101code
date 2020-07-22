# blur.py

from PIL import Image
from PIL import ImageFilter


def blur(path, modified_photo):
    image = Image.open(path)
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(modified_photo)

if __name__ == '__main__':
    blur('butterfly.jpg', 'butterfly_blurred.jpg')