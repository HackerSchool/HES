import serial
import pyautogui

ser = serial.Serial('/dev/ttyACM0', 9600)

btnnames = {
        0: 'start',
        1: 'select',
        2: 'A',
        3: 'B',
        4: 'up',
        5: 'right',
        6: 'down',
        7: 'left',
        }

conv = {0: 'enter',
        1: 'esc',
        2: 'v',
        3: 'c',
        4: 'w',
        5: 'd',
        6: 's',
        7: 'a',
        }

while True:
    # read a single code from the controller
    code = ser.read()
    # convert it to an int
    #code = code.decode('ascii')
    code = int.from_bytes(code, byteorder='little')

    # decompose the code in parts
    updown = code>>3 & 1
    btnid = code & 7

    print(updown, btnid)
    if(updown):
        print(conv[btnid], "up")
        pyautogui.keyUp(conv[btnid])
    else:
        print(conv[btnid], "down")
        pyautogui.keyDown(conv[btnid])

