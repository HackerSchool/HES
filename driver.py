import serial

ser = serial.Serial('/dev/ttyUSB0', 9600)

conv = {'0': 'start',
        '1': 'select',
        '2': 'A',
        '3': 'B',
        '4': 'up',
        '5': 'right',
        '6': 'down',
        '7': 'left',
        }

while True:
    code = ser.read()
    code = code.decode('ascii')

    print(conv[code])
