import serial

ser = serial.Serial('/dev/ttyACM0', 9600)

conv = {0: 'start',
        1: 'select',
        2: 'A',
        3: 'B',
        4: 'up',
        5: 'right',
        6: 'down',
        7: 'left',
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
    else:
        print(conv[btnid], "down")

