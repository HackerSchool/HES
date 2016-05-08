import pkg_resources as pkg

gui = True

# Note: communication between the computer and the Arduino is in bytes (ASCII),
# so you should specify this by adding the 'b' (bytes) in front of the strings, otherwise Python 3 will use UTF-8
handshake_challenge = b"Hi. Who are you?"
handshake_response = b"Hi. I'm HES."

profiles_file_name = pkg.resource_filename(__name__, 'resources/profiles.json')
possible_keys = pkg.resource_filename(__name__, 'resources/possible_keys.json')
# want all the possible keys? http://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

debug_port_detection = False  # force the port to be used
forced_port = 'COM3'
baud_rate = 9600  # Must be set the same as on the Arduino. It configures the speed of communication.

poll_delay = 0.001  # the delay between blocking on reading from the controller (seconds)

button_names = {'0': 'select',
                '1': 'start',
                '2': 'up',
                '3': 'down',
                '4': 'left',
                '5': 'right',
                '6': 'a',
                '7': 'b'
                }
