import serial


ser = serial.Serial('/dev/cu.usbmodem1421', 115200)

while True:
    print(eval(ser.readline()))