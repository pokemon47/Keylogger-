from pynput import keyboard
from pynput.keyboard import Key, Controller
from pathvalidate import sanitize_filename
import sys
import time

# requires a command line arguement, the filename/path of where the keys are logged 


keyboardKeys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.', ',', '!', '?', ':', ';', '"', "'", '-', '_', '=', '+', '@', '#', '$', '%', '^', '&', '*', '(', ')', '[', ']', '{', '}', '\\', '/', '~']

stringToKey = {
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
"Key.home": Key.home,
"Key.insert": Key.insert,
"Key.left": Key.left,
"Key.menu": Key.menu,
"Key.num_lock": Key.num_lock,
"Key.page_down": Key.page_down,
"Key.page_up": Key.page_up,
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
    filename = fileCleaner()
    fileReader = open(filename, 'r')

    keyboard = Controller()
    global stringToKey

    time.sleep(5)
    pressedKeys = []
    for line in fileReader:
        print(line, end="")
        time.sleep(0.03)
        state = line.split()[0]
        if state == "WAIT":
            time.sleep(0.5)
            continue
        key = line.split()[1]

        if key[0] == "'" and len(key) == 3:
            key = key[1:]
            key = key[:-1]
        elif key in stringToKey:
            key = stringToKey[key]
        else:
            continue
        if (state == "pressed"):
            keyboard.press(key)
            pressedKeys.append(key)
        else:
            keyboard.release(key)
            copy = pressedKeys.copy()
            pressedKeys = [i for i in copy if i != key] 
    print(pressedKeys, end="")

def stringToKeys(value):
    keys = []
    for character in value:
        if character == " ":
            keys.append(f"pressed Key.space\n")
            keys.append(f"released Key.space\n")
        elif character == '\n':
            keys.append(f"pressed Key.enter\n")
            keys.append(f"released Key.enter\n")
        else:
            keys.append(f"pressed '{character}'\n")
            keys.append(f"released '{character}'\n")
    return keys

def fileCleaner():
    src = open(sys.argv[1], 'r')
    dest = open(f"_TEMP_{sys.argv[1]}", 'w')

    no = [
        "pressed Key.tab\n",
        "released Key.tab\n",
        "pressed Key.alt_l\n",
        "released Key.alt_l\n",
        "released Key.caps_lock\n",
        "pressed Key.caps_lock\n",
        "released Key.cmd\n",
        "pressed Key.cmd\n",
        "released Key.cmd_l\n",
        "pressed Key.cmd_l\n",
        "released Key.cmd_r\n",
        "pressed Key.cmd_r\n",
        "released Key.ctrl\n",
        "pressed Key.ctrl\n",
        "released Key.ctrl_l\n",
        "pressed Key.ctrl_l\n",
        "released Key.ctrl_r\n",
        "pressed Key.ctrl_r\n",
        "released Key.down\n",
        "pressed Key.down\n",
        "released Key.end\n",
        "pressed Key.end\n",
        "pressed Key.esc\n"
        "released Key.esc\n",
        "pressed Key.home\n",
        "released Key.home\n",
        "pressed Key.insert\n",
        "released Key.insert\n",
        "pressed Key.left\n",
        "released Key.left\n",
        "pressed Key.media_next\n",
        "released Key.media_next\n",
        "pressed Key.media_play_pause\n",
        "released Key.media_play_pause\n",
        "pressed Key.media_previous\n",
        "released Key.media_previous\n",
        "pressed Key.media_volume_down\n",
        "released Key.media_volume_down\n",
        "pressed Key.media_volume_mute\n",
        "released Key.media_volume_mute\n",
        "pressed Key.media_volume_up\n",
        "released Key.media_volume_up\n",
        "pressed Key.menu\n",
        "released Key.menu\n",
        "pressed Key.num_lock\n",
        "released Key.num_lock\n",
        "pressed Key.page_down\n",
        "released Key.page_down\n",
        "pressed Key.page_up\n",
        "released Key.page_up\n",
        "pressed Key.pause\n",
        "released Key.pause\n",
        "pressed Key.print_screen\n",
        "released Key.print_screen\n",
        "pressed Key.right\n",
        "released Key.right\n",
        "pressed Key.scroll_lock\n",
        "released Key.scroll_lock\n",
        "pressed Key.shift\n",
        "released Key.shift\n",
        "pressed Key.shift_l\n",
        "released Key.shift_l\n",
        "pressed Key.shift_r\n",
        "released Key.shift_r\n",
        "pressed Key.up\n",
        "released Key.up\n"
        ]

    before = [
        "pressed Key.ctrl_l\n",
        "pressed 's'\n",
        "released 's'\n",
        "released Key.ctrl_l\n",
        "pressed Key.ctrl_l\n",
        "pressed 'w'\n"
        "released 'w'\n"
        "released Key.ctrl_l\n",
        "pressed Key.ctrl_l\n",
        "pressed Key.shift_l\n",
        "pressed '`'\n",
        "released '`'\n",
        "released Key.shift_l\n",
        "released Key.ctrl_l\n",
        "pressed 'c'\n",
        "released 'c'\n",
        "pressed 'o'\n",
        "released 'o'\n",
        "pressed 'd'\n",
        "released 'd'\n",
        "pressed 'e'\n",
        "released 'e'\n",
        "pressed Key.space\n",
        "released Key.space\n",
    ]

    after = [
        "pressed Key.enter\n",
        "released Key.enter\n",
        "WAIT\n",
        "pressed Key.ctrl_l\n",
        "pressed 's'\n"
        "released 's'\n"
        "released Key.ctrl_l\n",
        "pressed Key.ctrl_l\n",
        "pressed '`'\n"
        "released '`'\n"
        "released Key.ctrl_l\n",
        "pressed Key.ctrl_l\n",
        "pressed Key.shift_l\n",
        "pressed 'k'\n"
        "released 'k'\n"
        "released Key.shift_l\n",
        "released Key.ctrl_l\n",
    ]

    buffer = []
    for line in src:
        diff = line.split()[0]
        if ((diff == "pressed" or diff == "released") and line.split()[1][0] == "'" and len(line.split()[1]) > 3) or ((diff == "pressed" or diff == "released") and line.split()[1][0] != "'" and line.split()[1].split('.')[0] != "Key"):
            continue
        elif (diff == "pressed" or diff == "released") and buffer == []:
            dest.write(line)
        elif (diff == "pressed" or diff == "released") and (buffer != []) and (line not in no):
            filename = "'" + sanitize_filename(buffer[0]) + "'"
            toWrite = before + stringToKeys(filename) + after + buffer[1:]
            toWrite = before + stringToKeys(filename) + after + buffer[1:]
            for lineToWrite in toWrite:
                dest.write(lineToWrite)
            buffer = []
            dest.write(line)
        elif (diff == "pressed" or diff == "released") and (buffer != []) and (line in no):
            buffer.append(line)
        else:
            buffer = [line]
    for line in after:
        dest.write(line)
    src.close()
    dest.close()
    return f"_TEMP_{sys.argv[1]}"
main()