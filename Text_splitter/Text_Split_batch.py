#!/usr/bin/env python3

import numpy as np
from PIL import Image
from DirectoryTransversal import file_search


def get_img_snip(img, size=(50, 50)):
    im_array = np.asarray(img)
    return Image.fromarray(im_array[0:size[0], 0:size[1], :])


def create_snippets(file_list, file_term = 'snip'):
    for file_name in file_list:
        raw_img = Image.open(file_name).convert('RGBA')
        snip = get_img_snip(raw_img, (170, 170))
        snip.save(file_name.split('.png')[0] + '_' + file_term + '.png')



if __name__ == '__main__':
    file_terminations = (
        'gravel.png'
        #'_wool.png',
        #'_carpet.png'
    )

    directory = '/home/js/.minecraft/resourcepacks/NAPP_512_2/assets/minecraft/textures/block/'
    file_dirs = file_search(file_terminations, directory)
    create_snippets(file_dirs)
