# External
import pyautogui
from time import sleep

# Internal
from controller_communication import HESInterface
from button_bindings import ButtonBindings


pyautogui.PAUSE = 0
button_bindings = ButtonBindings()
with HESInterface() as controller:
    while True:
        status, button = controller.read_data()
        key = button_bindings.translate_button(button)
        if key:
            if status == 'P':
                pyautogui.keyDown(key)
            if status == 'R':
                pyautogui.keyUp(key)
            key = None
            sleep(0.001)
