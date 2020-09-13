import platform
import time
from enum import Enum
from pynput.keyboard import Key, Controller

'''
    Util for rotating the player, and taking snapshots, in order to take
    the panoramic screen caps. This is possible via keyboard control.
    by Juan S. Marquerie

    TODO:
        -Add singleton for all the keyoard instances
'''

# All the direction needed
class Player_Dirs(Enum):
    FRONT = '~1 ~ ~'
    LEFT  = '~ ~ ~-1'
    RIGHT = '~ ~ ~1'
    BACK  = '~-1 ~ ~'
    UP    = '~ ~1 ~'
    DOWN  = '~ ~-1 ~'

# Rotate player to one of the directions
def player_rotate(direction='~ ~ ~'):
    keyboard = Controller()
    command = 'tp @a ~ ~ ~ ' + direction.value

    print('Writing ' + command)
    keyboard.press('/')
    keyboard.release('/')
    time.sleep(0.5)
    keyboard.type(command)

# Toggle minecraft UI
def toggle_UI():
    print('Toggled UI')
    keyboard = Controller()
    keyboard.press(Key.f1)
    keyboard.release(Key.f1)

# Take a snapshot
def take_snapshot():
    print('Take snapshot')
    keyboard = Controller()

    keyboard.press(Key.f2)
    keyboard.release(Key.f2)

# Print a message on minecraft
def message(msg=''):
    command = '/msg @a ' + msg
    keyboard = Controller()

    print('Printed ' + command + ' on minecraft')
    keyboard.type(command)