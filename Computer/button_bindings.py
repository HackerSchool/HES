def button_binding(pressed_button):
    button_names = {'0': 'select',
                    '1': 'start',
                    '2': 'up',
                    '3': 'down',
                    '4': 'left',
                    '5': 'right',
                    '6': 'a',
                    '7': 'b'
                    }

    bindings = {'up': 'w',
                'down': 's',
                'left': 'a',
                'right': 'd',
                'a': 'space',
                'b': 'f',
                'select': 'esc',
                'start': 'enter'
                }
    try:
        return bindings[button_names[pressed_button]]
    except KeyError:
        print('BAM')
        return None
