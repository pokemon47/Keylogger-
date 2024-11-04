from pynput import keyboard
from pynput.keyboard import Key, Controller
import sys
import time
import pyperclip

import requests
keyboard = Controller()

# time.sleep(3)

# value = 'v'
# # value = value[1:]
# # value = value[:-1]
# with keyboard.pressed(Key.ctrl_l):
#     with keyboard.pressed(Key.shift_l):

#         keyboard.press(Key.end)
#         keyboard.release(Key.end)
#         print('hi')

# keyboard.press(Key.delete)
# keyboard.release(Key.delete)
    
# def multiKeyPress(keys):
#     keyboard = Controller()
#     # for keyValue in keys:
#     #     keyboard.press(keyValue)
#     for keyValue in keys[::-1]:
#         keyboard.release(keyValue)
# multiKeyPress([Key.ctrl_l, Key.shift_l, Key.end])

# recent_value = ""
# while True:
#     tmp_value = pyperclip.paste()
#     if tmp_value != recent_value:
#         recent_value = tmp_value
#         # print("Value changed: %s" % str(recent_value)[:20])
#         print(str(recent_value))
#     time.sleep(0.1)

# print(requests.post("http://127.0.0.1:5000/getClip"))
import datetime
def timeStamp():
    dt = datetime.datetime.now()
    formatted_timestamp = dt.strftime("%Y-%m-%d-%Hh")
    return (formatted_timestamp)

def focusCapture ():
    from win32gui import GetWindowText, GetForegroundWindow
    print(GetWindowText(GetForegroundWindow()))
    curWindow = GetWindowText(GetForegroundWindow())
    while True:
        temp = GetWindowText(GetForegroundWindow())
        if temp != curWindow:
            curWindow = temp
            if temp and temp != "Task Switching":
                print(f"{timeStamp()} - {temp}")

# focusCapture()
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
    for val in keys[1:]:
        print(val, end="")
stringToKeys("code ")
