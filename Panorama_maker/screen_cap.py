import os
import time
import minecraft_control as mc_cont
from pathlib import Path
from minecraft_control import Player_Dirs
from DirectoryTransversal import file_search

'''
    Take in-game screen captures of minecraft
    by Juan S. Marquerie
'''

def take_screenshots(mc_folder_dir=''):
    mc_cont.toggle_UI()

    # Take a snapshot for each direction
    for dir in Player_Dirs:
        mc_cont.player_rotate(dir)
        mc_cont.take_snapshot()
        time.sleep(1)

    # Restore UI
    mc_cont.toggle_UI()

    # Find all the screenshots in the minecraft folder
    screen_shot_paths = sorted(Path(os.path.join(mc_folder_dir, 'screenshots')).iterdir(), key=os.path.getmtime)

    # Return the last 6 image dirs
    return screen_shot_paths[-6:]