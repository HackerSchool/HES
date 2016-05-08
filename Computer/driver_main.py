# External
import pyautogui  # pip install pillow; pip install pyautogui
from time import sleep
import threading

# Internal
from Computer.controller_communication import HESInterface
from Computer.button_bindings import ButtonBindings
import Computer.settings as settings


class DriverThread(threading.Thread):
    def __init__(self, bindings):
        super().__init__()
        self.bindings = bindings

    def run(self):
        run_driver(self.bindings)


def run_driver(button_bindings=ButtonBindings()):
    pyautogui.PAUSE = 0  # No delay when pressing/releasing keys
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
                sleep(settings.poll_delay)

if __name__ == '__main__':
    run_driver()