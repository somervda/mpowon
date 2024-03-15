from machine import UART,Pin
import time

uart = UART(0, baudrate=115200, tx=Pin(16), rx=Pin(17))     # init uart 0
uart.init(bits=8, parity=None, stop=1)
# clear uart
uart.read()

# Send ID request and show result
#  see https://pallavaggarwal.in/owon-xdm1041-programmable-multimeter/#SCPI_Commands
uart.write('*IDN?\n')
time.sleep(1)
details = uart.read()
print("Details:",details)

# Get current measuerment
for x in range(20):
    uart.write('MEAS1:SHOW?\n')
    time.sleep(1)
    measurement = uart.read()
    print("Measurement:",measurement)