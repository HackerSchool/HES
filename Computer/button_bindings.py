import json
import settings


class ButtonBindings:
    """
    This class handles the button profiles. It can translate a button to its mapped key
     and create/modify/delete profiles.
    """
    def __init__(self, current_profile='default'):
        self.button_names = settings.button_names
        self.profiles = self.load_profiles()
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
        json.dump(self.profiles, open(settings.profiles_file_name, 'w'))

    @staticmethod
    def load_profiles():
        return json.load(open(settings.profiles_file_name))

    def reload_profiles(self):
        self.profiles = self.load_profiles()

    def get_profile_names(self):
        return list(self.profiles.keys())

    def choose_profile(self, profile_name):
        self.current_profile = profile_name

    def get_current_profile(self):
        return self.profiles[self.current_profile]

    def edit_binding(self, button, key):
        if self.current_profile == 'default':
            print("can't edit the default profile")
        else:
            self.profiles[self.current_profile][button] = key

    def create_profile(self, profile_name, profile):
        if profile_name == 'default':
            print("can't overwrite the default profile")
        else:
            self.profiles[profile_name] = profile

    def remove_profile(self, profile_name):
        if profile_name == 'default':
            print("can't delete the default profile")
        else:
            del self.profiles[profile_name]


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
    json.dump(profiles, open(settings.profiles_file_name, 'w'))
