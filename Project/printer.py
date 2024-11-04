from pynput import keyboard
import time

f = open("log2.txt", "a")

def main():
    # Spawning the thread to write to the log file every 5 seconds.
    with keyboard.Listener(on_press=recordPress, on_release=recordRelease) as listener:
        listener.join()


def recordPress(key):
    global f
    # f.write(f"pressed {int(time.time())} {key}\n")
    
    if str(key) == r"'\x16'":
        print("PASTED HEREE")
    # print(str(key))
    # print(r"'\x16'")
    print(f"pressed {key}")
def recordRelease(key):
    global f
    # f.write(f"released {int(time.time())} {key}\n")
    # print(f"released {key}")

if __name__=="__main__":
    main()