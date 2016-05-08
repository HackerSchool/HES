# External
import json

# Internal
import Computer.settings as settings


class ButtonBindings:
    """
    This class handles the button profiles. It can translate a button to its mapped key
     and create/modify/delete profiles.
    """
    def __init__(self, current_profile='default'):
        self.profiles = None
        self.button_names = settings.button_names
        self.load_profiles()
        self.current_profile = current_profile

    def translate_button(self, pressed_button):
        try:
            bindings = self.profiles[self.current_profile]
            button_name = self.button_names[pressed_button]
            return bindings[button_name]

        except KeyError:
            print('BAM')
            return None

    def store_profiles(self):
        with open(settings.profiles_file_name, 'w') as profiles_file:
            json.dump(self.profiles, profiles_file)

    def load_profiles(self):
        with open(settings.profiles_file_name, 'r') as profiles_file:
            self.profiles = json.load(profiles_file)

    def get_profile_names(self):
        return list(self.profiles.keys())

    def choose_profile(self, profile_name):
        self.current_profile = profile_name

    def get_current_profile(self):
        return self.profiles[self.current_profile]

    def get_binding(self, button):
        return self.profiles[self.current_profile][button]

    def edit_binding(self, button, key):
        self.profiles[self.current_profile][button] = key

    def create_profile(self, profile_name, profile):
        self.profiles[profile_name] = profile

    def remove_profile(self, profile_name):
        if profile_name == 'default':
            print("can't delete the default profile")
        else:
            del self.profiles[profile_name]
            self.current_profile = None
            self.store_profiles()

    @staticmethod
    def get_possible_keys():
        with open(settings.possible_keys, 'r') as possible_keys_file:
            return json.load(possible_keys_file)


if __name__ == '__main__':
    # in case the file becomes corrupted, run this file to recreate it with the default profile
    profiles = {'default': {'up': 'w',
                            'down': 's',
                            'left': 'a',
                            'right': 'd',
                            'a': 'v',
                            'b': 'c',
                            'select': 'esc',
                            'start': 'space'
                            },
                }
    with open(settings.profiles_file_name, 'w') as file:
        json.dump(profiles, file)
