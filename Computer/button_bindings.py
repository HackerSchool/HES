import json
import settings


class ButtonBindings:
    def __init__(self, current_profile='default'):
        self.button_names = {'0': 'select',
                             '1': 'start',
                             '2': 'up',
                             '3': 'down',
                             '4': 'left',
                             '5': 'right',
                             '6': 'a',
                             '7': 'b'
                             }

        self.current_profile = current_profile
        self.profiles = {'default': {'up': 'w',
                                     'down': 's',
                                     'left': 'a',
                                     'right': 'd',
                                     'a': 'v',
                                     'b': 'c',
                                     'select': 'esc',
                                     'start': 'space'
                                     },
                         }

        self.reload_profiles()

    def translate_button(self, pressed_button):
        try:
            bindings = self.profiles[self.current_profile]
            button_name = self.button_names[pressed_button]
            return bindings[button_name]

        except KeyError:
            print('BAM')
            return None

    def store_profiles(self):
        json.dump(self.profiles, open(settings.profiles_file_name, 'w'))

    def reload_profiles(self):
        self.profiles = json.load(open(settings.profiles_file_name))

    def choose_profile(self, profile_name):
        self.current_profile = profile_name

    def create_profile(self, profile_name, profile):
        self.profiles[profile_name] = profile

    def remove_profile(self, profile_name):
        if profile_name == 'default':
            print("can't delete the default profile")
        del self.profiles[profile_name]

