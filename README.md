Open the magnetometer.io file in arduino.ide

Connect the board of your choice to your computer via a serial port or usb port

Download the esp32 and mlx9039 libraries if you have not done so already

Go to the wire.begin statement and change it's arguments to be the output lines of your sda and scl ports respectively.
Upload the program to the arduino 
Open the Magnetometer_readings.py since you will need it to query the serial port
In  Magnetometer_readings.py , replace basic_test.txt with a file name that you would like to save to.
Change the argument of serial.Serial to the name of the port that arduino is connected to.
Start the python program and you should begin having the file read data and you are all set
