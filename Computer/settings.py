handshake_challenge = b"Hi. Who are you?"
handshake_response = b"Hi. I'm HES."

gui = True
profiles_file_name = 'profiles.json' if not gui else '../profiles.json'
possible_keys = '../possible_keys.json'
# want all the possible keys? http://pyautogui.readthedocs.io/en/latest/keyboard.html#keyboard-keys

debug_port_detection = False
forced_port = 'COM3'
baud_rate = 9600

button_names = {'0': 'select',
                '1': 'start',
                '2': 'up',
                '3': 'down',
                '4': 'left',
                '5': 'right',
                '6': 'a',
                '7': 'b'
                }

