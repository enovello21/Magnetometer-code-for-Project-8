#Project 8 Magnetometer
# Made by Eric Novello and Professor Walter Pettus June 4 2024
#This code is to be used alongside an arduino running off magnetometer
#code found in the same github page as this. 
import serial
from serial.tools.list_ports import comports
import datetime
import time
Basic_test = open("Basic_test.txt", "w")
Basic_test.write("Magnetic fields are written in µT")
Basic_test.write('\n')
Basic_test.close()
ports = [x.device for x in comports() if 'usbserial' in x.device]
myserial = serial.Serial(ports[0], baudrate=115200)
while True:
    Basic_test = open("Basic_test.txt", "a")
    #print(datetime.datetime.now())
    Basic_test.write(str(datetime.datetime.now()))
    myserial.write("\n".encode())
    thisdata = myserial.read_until(b'XXX\r\n').decode().rstrip('\r\nXXX\r\n')
    #print(repr(thisdata))
    Basic_test.write(" ")
    Basic_test.write(str(thisdata))
    Basic_test.write('\n')
    Basic_test.close()
