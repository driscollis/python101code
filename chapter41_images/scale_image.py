# scale_image.py

from PIL import Image

def scale_image(input_image_path,
                output_image_path,
                width=None,
                height=None
                ):
    original_image = Image.open(input_image_path)
    w, h = original_image.size
    print(f'The original image size is {w} wide x {h} '
          'high')

    if width and height:
        max_size = (width, height)
    elif width:
        max_size = (width, h)
    elif height:
        max_size = (w, height)
    else:
        # No width or height specified
        raise ValueError('Width or height required!')

    original_image.thumbnail(max_size, Image.ANTIALIAS)
    original_image.save(output_image_path)

    scaled_image = Image.open(output_image_path)
    width, height = scaled_image.size
    print(f'The scaled image size is {width} wide x {height} '
          'high')


if __name__ == '__main__':
    scale_image(input_image_path='lizard.jpg',
                output_image_path='lizard_scaled.jpg',
                width=800)