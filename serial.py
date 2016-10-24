import serial


class Serial:
    def __init__(self, port, baud):
        self.port = port
        self.baud = baud
        self.serial = None
        self.connect()

    def connect(self):
        self.serial = serial.Serial(
            port=self.port,
            baudrate=self.baud,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=3
        )

    def disconnect(self):
        self.serial.close()

    def send(self, command):
        self.serial.write(bytes(command + '\n', 'utf-8'))
        response = self.serial.readline()

        return response.decode('utf-8').rstrip()
