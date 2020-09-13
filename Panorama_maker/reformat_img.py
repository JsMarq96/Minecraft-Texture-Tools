from PIL import Image
import numpy as np

'''
    Helper function to format the image as a centerd square,
    for the panoramic images
    bu Juan S. Marquerie
'''

def reformat(original_image, destination_image):
    raw_image = np.asarray(Image.open(original_image).convert('RGBA'))

    im_heigh, im_width, _ = raw_image.shape

    center_x = int(im_width / 2.0)
    final_size_half = int(im_heigh / 2.0)

    final_img = raw_image[:, center_x - final_size_half : center_x + final_size_half, :]

    Image.fromarray(final_img.astype(np.uint8)).save(destination_image)