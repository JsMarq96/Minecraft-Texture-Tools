from PIL import Image
import numpy as np 

'''
    Funtions for overlaying 2 images or textures,
    with a given mask.
    by Juan S. Marquerie
'''
def add_overlay_channel(base_channel, overlay_channel, mask):
    return overlay_channel + np.multiply(base_channel, 1-mask)

def add_overlay_channel_with_inverted_mask(base_channel, overlay_channel, mask):
    return np.multiply(overlay_channel, mask) + np.multiply(base_channel, 1-mask)

def add_overlay(img, overlay, mask, maintain_base_alpha = False):
    _, _, img_dims = img.shape
    result = np.zeros(img.shape)

    if maintain_base_alpha:
        img_dims = img_dims - 1
        result[:,:,3] = img[:,:,3]

    for dim in range(img_dims):
        result[:,:,dim] = add_overlay_channel(img[:,:,dim], overlay[:,:,dim], mask)

    return result

def add_overlay_with_inverted_mask(img, overlay, mask, maintain_base_alpha = False):
    _, _, img_dims = img.shape
    result = np.zeros(img.shape)

    if maintain_base_alpha:
        img_dims = img_dims - 1
        result[:,:,3] = img[:,:,3]

    for dim in range(img_dims):
        result[:,:,dim] = add_overlay_channel_with_inverted_mask(img[:,:,dim], overlay[:,:,dim], mask)

    return result

def overlay_texture(base_img, overlay_img):
    # Use the overlay's alpha channel as the overlay mask
    mask = overlay_img[:,:,3] / 255
    return add_overlay(base_img, overlay_img, mask)