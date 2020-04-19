import serial
import glob

ports = glob.glob('/dev/tty[A-Za-z]*')
result = []
for port in ports:
    try:
        s = serial.Serial(port)
        s.close()
        result.append(port)
    except (OSError, serial.SerialException):
        pass
print(result)

ser = serial.Serial(result[0])
ser.baudrate = 115200
 
# while True :
#   line = ser.readline()
#   print(line)

def read_usb():
    line = ser.readline()
    yield line
for i in range(10):

    cv = next(read_usb())
    print(cv)
