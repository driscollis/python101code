# get_image_info.py

from PIL import Image

def get_image_info(path):
    image = Image.open(path)
    print(f'This image is {image.width} x {image.height}')
    exif = image._getexif()
    print(exif)

if __name__ == '__main__':
    get_image_info('ducks.jpg')