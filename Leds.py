from pyfirmata import Arduino
import time
board = Arduino("COM7")
Ledve = board.get_pin('d:13:o')
Ledam = board.get_pin('d:12:o')
Ledred = board.get_pin('d:11:o')

while True:
    Ledred.write(1)
    time.sleep(4)
    Ledve.write(0)
    time.sleep(6)

    Ledam.write(1)
    time.sleep(1)
    Ledve.write(0)
    time.sleep(3)

    Ledve.write(1)
    time.sleep(3)
    Ledve.write(0)
    time.sleep(6)
