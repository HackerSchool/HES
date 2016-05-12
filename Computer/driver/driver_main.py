# External
import threading
from time import sleep
import pyautogui  # pip install pillow; pip install pyautogui;

# Internal
from Computer.driver.controller_communication import HESInterface
from Computer.driver.button_bindings import ButtonBindings
import Computer.settings as settings


# Standard Python thread class, used so the driver can run in parallel with the gui
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
                    # Note: Don't worry if by holding down the button it doesn't repeat the key in a text editor.
                    # The key is held down (try it in a game) but it isn't firing periodic keyDown()'s like keyboards do
                if action == 'R':  # released
                    pyautogui.keyUp(key)

                sleep(settings.poll_delay)


if __name__ == '__main__':
    run_driver()
