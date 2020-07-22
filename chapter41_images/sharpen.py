# sharpen.py

from PIL import Image
from PIL import ImageFilter


def sharpen(path, modified_photo):
    image = Image.open(path)
    blurred_image = image.filter(ImageFilter.SHARPEN)
    blurred_image.save(modified_photo)

if __name__ == '__main__':
    sharpen('butterfly.jpg', 'butterfly_sharper.jpg')