# get_histrogram.py

import matplotlib.pyplot as plt

from PIL import Image


def get_image_histrogram(path):
    image = Image.open(path)
    histogram = image.histogram()
    plt.hist(histogram, bins=len(histogram))
    plt.xlabel('Histogram')
    plt.show()

if __name__ == '__main__':
    get_image_histrogram('butterfly.jpg')