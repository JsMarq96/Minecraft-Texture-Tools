import platform
import time
from enum import Enum
from pywinauto import keyboard

'''
    Util for rotating the player, and taking snapshots, in order to take
    the panoramic screen caps. This is possible via keyboard control.
    by Juan S. Marquerie
'''

# All the direction needed
class Player_Dirs(Enum):
    FRONT = '~1 ~ ~'
    LEFT  = '~ ~ ~-1'
    RIGHT = '~ ~ ~1'
    BACK  = '~-1 ~ ~'
    UP    = '~ ~1 ~'
    DOWN  = '~ ~-1 ~'

def keyboard_simulate(text):
    buffer_text = ''
    for char in text:
        if char == ' ':
            buffer_text = buffer_text + '{SPACE}'
        elif char == '~':
            buffer_text = buffer_text + '{~}'
        elif char == '@':
            buffer_text = buffer_text + '{@}'
        elif char == '\n':
            buffer_text = buffer_text + '{ENTER}'
        elif char == '/':
            buffer_text = buffer_text + '+{' + char + ' down}{' + char + ' up}'
        else:
            buffer_text = buffer_text + '{' + char + ' down}{' + char + ' up}'
            print(buffer_text)
    print('buff', buffer_text)
    keyboard.send_keys(buffer_text)

# Rotate player to one of the directions
def player_rotate(direction='~1 ~ ~'):
    command = 't/tp @a ~ ~ ~ facing ' + direction.value + '\n'

    print('Writing ' + command)
    keyboard_simulate(command)

# Toggle minecraft UI
def toggle_UI():
    print('Toggled UI')

    keyboard.send_keys('{F1}')

# Take a snapshot
def take_snapshot():
    print('Take snapshot')
    
    keyboard.send_keys('{F2}')

# Print a message on minecraft
def message(msg=''):
    command = '/msg{SPACE}@a{SPACE}' + msg

    print('Printed ' + command + ' on minecraft')