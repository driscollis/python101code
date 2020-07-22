# resize_image.py

from PIL import Image

def resize_image(input_image_path,
                 output_image_path,
                 size):
    original_image = Image.open(input_image_path)
    width, height = original_image.size
    print(f'The original image size is {width} wide x {height} '
          f'high')

    resized_image = original_image.resize(size)
    width, height = resized_image.size
    print(f'The resized image size is {width} wide x {height} '
          f'high')
    resized_image.show()
    resized_image.save(output_image_path)

if __name__ == '__main__':
    resize_image(input_image_path='lizard.jpg',
                 output_image_path='lizard_small.jpg',
                 size=(800, 400))