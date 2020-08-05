from PIL import Image
import numpy as np 
from TextureOverlayer import add_overlay, add_overlay_with_inverted_mask

'''
    Functions for loading, formating and overlapping
    Optifine formated PBR texture maps
    but Juan S. Marquerie
'''

# Indexes for the PBR format
COLOR = 0
NORMALS = 1
SPECULAR = 2

'''
    Main overlapping function for PBR formated images
'''
def PBR_batch_overlaping(imgs, overlays):
    # We get the mask from the overlay's specular's alpha channel
    spec_overlay_mask = overlays[SPECULAR, :, :, 3] / 255.0
    color_overlay_mask = overlays[COLOR, :, :, 3] / 255.0
    results = np.zeros(imgs.shape)

    results[SPECULAR ,:,:,:] = add_overlay_with_inverted_mask(imgs[SPECULAR ,:,:,:], overlays[SPECULAR, :,:,:], spec_overlay_mask, True)
    results[COLOR ,:,:,:] = add_overlay_with_inverted_mask(imgs[COLOR ,:,:,:], overlays[COLOR, :,:,:], color_overlay_mask, True)
    results[NORMALS ,:,:,:] = add_overlay_with_inverted_mask(imgs[NORMALS ,:,:,:], overlays[NORMALS, :,:,:], color_overlay_mask)

    return results

'''
    Loads the Optifine friendly texture maps (of differenti images)
    and concatenates them into a single 4-N dimensional matrix
'''
def load_PBR_images(base_name, img_format='.png'):
    # Load the texture maps
    color_map = np.asarray(Image.open(base_name + img_format).convert('RGBA'))
    specular_map = np.asarray(Image.open(base_name + '_s' + img_format).convert('RGBA'))
    normals_map = np.asarray(Image.open(base_name + '_n' + img_format).convert('RGBA'))

    c_w, c_h, c_c = color_map.shape

    # Allocate space and fill it
    pbr_images = np.zeros((3, c_w, c_h, c_c))

    pbr_images[COLOR, :, :, :] = color_map
    pbr_images[SPECULAR, :, :, :] = specular_map
    pbr_images[NORMALS, :, :, :] = normals_map
    
    return pbr_images

'''
    Saves a PBR matrix, in the Optifine friendly format
'''
def save_PBR_images(pbr_img, name, img_format='.png'):
    Image.fromarray(pbr_img[COLOR].astype(np.uint8)).save(name + img_format)
    Image.fromarray(pbr_img[SPECULAR].astype(np.uint8)).save(name + '_s' + img_format)
    Image.fromarray(pbr_img[NORMALS].astype(np.uint8)).save(name + '_n' + img_format)

'''
    For testing:
'''
if __name__ == '__main__':
    names = ['diamond_ore']

    for name in names:
        overlay_img = load_PBR_images('NAPPs/ores/diamond/' + name)

        for e_i, i in enumerate(range(4)):
            for e_j, j in enumerate(range(4)):
                index = str((e_i * 16) + (e_j))
                base_img = load_PBR_images('NAPPs/stone/' + index)

                merged = PBR_batch_overlaping(base_img, overlay_img)

                save_PBR_images(merged, 'NAPPs/result/' + name + '/' + index)