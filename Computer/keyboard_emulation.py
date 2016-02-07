# External
import pyautogui
from time import sleep

# Internal
from controller_communication import HESInterface
from button_translation import translate_button


pyautogui.PAUSE = 0
with HESInterface() as controller:
    while True:
        key = translate_button(controller.read_data())
        if key:
            pyautogui.press('a')
            key = None
            sleep(0.1)
