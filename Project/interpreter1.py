from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import time

keyboardKeys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.', ',', '!', '?', ':', ';', '"', "'", '-', '_', '=', '+', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '\\', '/', '~']

stringToKey = {
# "Key.alt": Key.alt,
# "Key.alt_gr": Key.alt_gr,
# "Key.alt_l": Key.alt_l,
# "Key.alt_r": Key.alt_r,
"Key.backspace": Key.backspace,
"Key.caps_lock": Key.caps_lock,
"Key.cmd": Key.cmd,
"Key.cmd_l": Key.cmd_l,
"Key.cmd_r": Key.cmd_r,
"Key.ctrl": Key.ctrl,
"Key.ctrl_l": Key.ctrl_l,
"Key.ctrl_r": Key.ctrl_r,
"Key.delete": Key.delete,
"Key.down": Key.down,
"Key.end": Key.end,
"Key.enter": Key.enter,
"Key.esc": Key.esc,
# "Key.f1": Key.f1,
"Key.home": Key.home,
"Key.insert": Key.insert,
"Key.left": Key.left,
# "Key.media_next": Key.media_next,
# "Key.media_play_pause": Key.media_play_pause,
# "Key.media_previous": Key.media_previous,
# "Key.media_volume_down": Key.media_volume_down,
# "Key.media_volume_mute": Key.media_volume_mute,
# "Key.media_volume_up": Key.media_volume_up,
"Key.menu": Key.menu,
"Key.num_lock": Key.num_lock,
"Key.page_down": Key.page_down,
"Key.page_up": Key.page_up,
# "Key.pause": Key.pause,
# "Key.print_screen": Key.print_screen,
"Key.right": Key.right,
"Key.scroll_lock": Key.scroll_lock,
"Key.shift": Key.shift,
"Key.shift_l": Key.shift_l,
"Key.shift_r": Key.shift_r,
"Key.space": Key.space,
"Key.tab": Key.tab,
"Key.up": Key.up}

def multiKeyPress(keys):
    keyboard = Controller()
    keysReversed = keys[::-1]
    for keyValue in keys:
        keyboard.press(keyValue)
    for keyValue in keysReversed:
        keyboard.release(keyValue)


def main():
    fileReader = open(sys.argv[1], 'r')

    keyboard = Controller()
    global stringToKey

    time.sleep(5)
    pressedKeys = []
    for line in fileReader:
        time.sleep(0.02)
        state = line.split()[0]
        key = line.split()[1]
        if key[0] == "'" and len(key) == 3:
            key = key[1:]
            key = key[:-1]
        elif key in stringToKey:
            key = stringToKey[key]
        else:
            continue
        print(state, key)
        if (state == "pressed"):
            keyboard.press(key)
            pressedKeys.append(key)
        else:
            keyboard.release(key)
            copy = pressedKeys.copy()
            pressedKeys = [i for i in copy if i != key] 
    print(pressedKeys)
main()