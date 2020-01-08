# proof of concept
# recibe los datos via serial y guarda en un cvs
import serial
serialPort = serial.Serial(port= "/dev/ttyACM0", baudrate = 115200, timeout=1000)
file=open("whatitis.cvs","a")
while True:
    file.write(str(serialPort.readline())[2:][:-5])
    file.write("\n")
