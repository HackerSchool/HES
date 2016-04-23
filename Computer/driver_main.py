# External
import pyautogui  # pip install pillow; pip install pyautogui

# Internal
from controller_communication import HESInterface
from button_bindings import ButtonBindings

pyautogui.PAUSE = 0  # No delay when pressing/releasing keys
button_bindings = ButtonBindings()

with HESInterface() as controller:
    while True:
        action, button = controller.read_data()
        key = button_bindings.translate_button(button)
        if key:
            if action == 'P':  # pressed
                pyautogui.keyDown(key)
            if action == 'R':  # released
                pyautogui.keyUp(key)
            key = None
