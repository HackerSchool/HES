def translate_button(pressed_button):
    translations = {'up': 'w',
                    'down': 's',
                    'left': 'a',
                    'right': 'd',
                    'a': 'space',
                    'b': 'f',
                    'select': 'esc',
                    'start': 'enter'
                    }
    try:
        return translations[pressed_button]
    except KeyError:
        print('BAM')
        return None
