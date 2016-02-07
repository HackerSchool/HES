# External
import pyautogui
from time import sleep

# Internal
from controller_communication import HESInterface
from button_translation import translate_button

HES = HESInterface()

while True:
    key = translate_button(HES.read_data())
    if key:
        pyautogui.press(key)
        key = None
        sleep(0.1)

if __name__ == '__main__':

    sleep(1)
    pyautogui.typewrite('Hello world!', interval=0)
    pyautogui.typewrite('Hello world!', interval=0.1)
    pyautogui.press('left')
    pyautogui.keyDown('shift')
    pyautogui.typewrite(['left', 'left', 'left', 'left', 'left', 'left'])
    pyautogui.keyUp('shift')
    # pyautogui.hotkey('ctrl', 'shift', 'esc')
