from PIL import Image
from DirectoryTransversal import file_search
import shutil
import numpy as np
import os.path

IMAGE_TYPES = ('.png', '.jpg')
IMAGE_DEPTHS = (8, 16, 32)

class Img8Bits:
    '''
        Utility for changing the color depth of all the selected nested folders Juan S. Marquerie
        Using the PIL library, apply bicubic interpolation in order to escale,
        or downscale the directory
    '''

    '''
        Function to set the bitdepth a single image, and save it
    '''
    def image_bit_change(self, img_adress, result_img_adress, new_depth):
        img = Image.open(img_adress).convert('RGBA')
        if new_depth == 8:
            res = Image.fromarray(np.asarray(img, dtype=np.uint8))
        elif new_depth == 16:
            res = Image.fromarray(np.asarray(img, dtype=np.uint16))
        elif new_depth == 32:
            res = Image.fromarray(np.asarray(img, dtype=np.uint32))
        res.save(result_img_adress)

    '''
        Function to clone a full folder directory, in order to scale it
    '''
    def directory_clone(self, directory, location='', depth=8):
        new_dir_name = os.path.join(location, os.path.basename(directory) + '_' + str(depth) + 'bits')
        print(new_dir_name)
        shutil.copytree(directory, new_dir_name)
        
        return new_dir_name

    '''
        Iterate throught a directory, and bit change all the images
        to the selected size
    '''
    def bit_change_directory(self, directory, img_depth):
        images_in_directory = file_search(IMAGE_TYPES, directory)

        print('Bit changing ' + str(len(images_in_directory)) + ' images...')
        for image in images_in_directory:
            print('Bit change image: ' + image)
            self.image_bit_change(image, image, img_depth)

    '''
        (Main function)
        Duplicates a directory and then bit change it
    '''
    def change_directory(self, directory, address='', img_depth = 8):
        new_dir = self.directory_clone(directory, address, img_depth)
        self.bit_change_directory(os.path.join(address,new_dir), img_depth)
