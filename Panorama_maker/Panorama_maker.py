import os
import time
import shutil
import screen_cap
import reformat_img
from minecraft_control import Player_Dirs, message as mc_message

'''
    Main file
    by Juan S. Marquerie
'''

# Dictionaray that relates each perspective to a filename
FILE_NAME = {
    Player_Dirs.FRONT: 'panorama_0.png',
    Player_Dirs.LEFT:  'panorama_3.png',
    Player_Dirs.RIGHT: 'panorama_1.png',
    Player_Dirs.BACK:  'panorama_2.png',
    Player_Dirs.UP:    'panorama_4.png',
    Player_Dirs.DOWN:  'panorama_5.png'
}

# Main funcion to create a panorama image
def make_panorama_imgs(mc_folder_location='.'):
    snapshots = screen_cap.take_screenshots(mc_folder_location)

    # Wait for minecfrat to download the images
    time.sleep(1)

    # Create the folder where we are going to stre all the imgs
    folder_location = os.path.join(mc_folder_location, 'background')
    shutil.rmtree(folder_location)
    os.mkdir(folder_location)

    mc_message('Starting the image modification, wait...')

    # For each img, format it, and store it with the name related
    # to the perspective in witch the snapshot whas taken
    for index, perspective in enumerate(Player_Dirs):
        folder_img_dir = os.path.join(folder_location, FILE_NAME[perspective])
        reformat_img.reformat(snapshots[index], folder_img_dir)

    mc_message('Finished the panoramic process')


if __name__ == '__main__':
    time.sleep(4)
    make_panorama_imgs('/home/js/.minecraft/')