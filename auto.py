import pyautogui
import keyboard
from time import sleep

def auto():
    while True:
        keyboard.wait('b')
        while not keyboard.is_pressed('n'):
            pyautogui.click()

sleep(1)
print("      .__                       .__  .__        __                 ")
sleep(0.1)
print("  _____|  |   _______  __   ____ |  | |__| ____ |  | __ ___________ ")
sleep(0.1)
print("/  ___/  |  /  _ \  \/ / _/ ___\|  | |  |/ ___\|  |/ // __ \_  __ ")
sleep(0.1)
print(" \___ \|  |_(  <_> )   /  \  \___|  |_|  \  \___|    <\  ___/|  | \/")
sleep(0.1)
print("/____  >____/\____/ \_/    \___  >____/__|\___  >__|_ \\___  >__|   ")
sleep(0.1)
print("     \/                        \/             \/     \/    \/       ")
sleep(0.1)

x = input("start y/n? ")
if x.lower() == "y":
    print("press b to start the auto clicking and n to stop")
    auto()
else:
    exit()