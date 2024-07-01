#Project 8 Magnetometer
# Made by Eric Novello and Professor Walter Pettus July 1, 2024
#This code is to be used alongside an arduino running off magnetometer code
#found in the same github page as this. 
import serial
from serial.tools.list_ports import comports
import datetime
import time
Basic_test = open("full_test.txt", "w")
Basic_test.write("Magnetic fields are written in µT")
Basic_test.write('\n')
Basic_test.close()
ports = [x.device for x in comports() if 'usbserial' in x.device]
myserial = serial.Serial(ports[0], baudrate=115200)
while True:
    Basic_test = open("full_test.txt", "a")
    Basic_test.write(str(datetime.datetime.now()))
    Basic_test.write('\n')
    myserial.write("\n".encode())
    #####
   #Copy and paste this functional block for the amount of probes you have.
   #Change variable name 'thisdata' to be unique for each copy of the block
    thisdata=myserial.readline().decode().rstrip('\r\nXXX\r\n')
    Basic_test.write(str(thisdata))
    Basic_test.write('\n')
    #######
    thisdata1=myserial.readline().decode().rstrip('\r\nXXX\r\n')
    Basic_test.write(str(thisdata1))
    Basic_test.write('\n')
    thisdata2=myserial.readline().decode().rstrip('\r\nXXX\r\n')
    Basic_test.write(str(thisdata2))
    Basic_test.write('\n')
    Basic_test.close()
