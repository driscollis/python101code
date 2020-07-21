# cropping.py

from PIL import Image


def crop_image(path, cropped_path):
    image = Image.open(path)
    cropped = image.crop((40, 590, 979, 1500))
    cropped.save(cropped_path)

if __name__ == '__main__':
    crop_image('ducks.jpg', 'ducks_cropped.jpg')