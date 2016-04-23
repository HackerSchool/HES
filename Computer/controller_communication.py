# External
from time import sleep
import serial  # pip install pyserial
from serial.tools import list_ports

# Internal
import settings


class HESInterface:
    """
     This class initiates the connection to the HES controller and reads button presses
    """

    def __init__(self):
        self.interface = self.find_serial_port()

    def read_data(self, block=True):
        while block:
            received = self.interface.readline().rstrip()
            if received != b'':
                data = received.decode()
                return data[0], data[1]

#    def send_data(self, data):
#        self.interface.write(data.encode())

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.interface.close()

    @staticmethod
    def find_serial_port():
        """
        tries to connect to all available serial ports, returns of first successful connection.
        exit if none works

        :return: serial interface object
        """
        if settings.debug_port_detection:
            for port in list_ports.comports():
                print('trying {}'.format(port[0]))

            return serial.Serial(settings.forced_port, settings.baud_rate, timeout=1)

        else:
            for port in (list_ports.comports()):
                print('trying {}'.format(port[0]))
                try:
                    serial_interface = serial.Serial(port[0], settings.baud_rate, timeout=2)
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


if __name__ == '__main__':
    with HESInterface() as HES:
        while True:
            print(HES.read_data())
