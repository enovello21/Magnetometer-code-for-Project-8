To use this file, open it in arduino.ide 
Connect the board of your choice to your computer via a serial port or usb port

Download the esp32 and mlx9039 libraries if you have not done so already

Go to the wire.begin statement and change it's arguments to be the output lines of your sda and scl ports respectively.
Upload the program to the arduino and open the serial monitor to see the readings of the magnetometer probes.

In the python code, replace basic_test.txt with a file name that you would like to save to. Then run the python program
