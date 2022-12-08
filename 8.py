import numpy as np
from PIL import Image

BLACK, WHITE = 0, 255

def get_image_pixels(filename):
    with Image.open(filename) as image:
        width, height = image.size
        return np.array(image.getdata()).reshape((height, width))

def find_X(pixels):
    """
    White shape center X coordinate is the white middle row.
    """
    white_rows = np.where(pixels == WHITE)[0]
    return (white_rows[0] + white_rows[-1]) // 2

def find_Y(pixels, X):
    """
    White shape center Y coordinate is the middle element index of the white middle row.
    """
    middle_row_white_pixels = np.where(pixels[X] == WHITE)[0]
    return (middle_row_white_pixels[0] + middle_row_white_pixels[-1]) // 2

filename = '8.png'
pixels = get_image_pixels(filename)
X = find_X(pixels)
Y = find_Y(pixels, X)
print(f'{X=},{Y=}')