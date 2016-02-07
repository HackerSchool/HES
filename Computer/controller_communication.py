# External
from time import sleep
import serial
from serial.tools import list_ports

# Internal
import settings


def find_serial_port():
    """
    tries to connect to all available serial ports, returns of first successful connection.
    exit if none works

    :return: serial interface object
    """
    if settings.debug_port_detection:
        for port in list_ports.comports():
            print('trying {}'.format(port[0]))

        return serial.Serial(settings.forced_port, 9600, timeout=1)

    else:
        for port in (list_ports.comports()):
            print('trying {}'.format(port[0]))
            try:
                serial_interface = serial.Serial(port[0], 9600, timeout=2)
                sleep(2)  # wait for the device to be ready
                # send hello command
                serial_interface.write(settings.handshake_challenge)

                # check if this device knows what to reply
                reply = serial_interface.read(len(settings.handshake_response))
                print(reply)
                if reply == settings.handshake_response:
                    return serial_interface

            except serial.SerialException:
                # print("opening serial failed")
                pass

    raise ConnectionError("Couldn't connect to any serial ports, exiting...")


class HESInterface:

    def __init__(self):
        self.interface = find_serial_port()

    def read_data(self, block=True):
        while block:
            received = self.interface.readline().rstrip()
            if received != b'':
                return received.decode()

#    def send_data(self, data):
#        self.interface.write(data.encode())

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.interface.close()


if __name__ == '__main__':
    HES = HESInterface()
    while True:
        print(HES.read_data())

