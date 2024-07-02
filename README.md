Open the magnetometer.io or MagnetometerPHT.io file in arduino.ide
MagnetometerPHT.io is able to read the Magnetometer data from multiple adafruit mlx90393 probes and from an adafruit ms8607 pressure, humidity, temperature probe.
These codes output data from the probes when queried by the Magneotmeter_readings python program.

SETUP INSTRUCTIONS
Arduino
Connect the board of your choice to your computer via a serial port or usb port
Download the libraries in the Magnetometer or MagnetometerPHT Arduino code if you have not done so already. 
Go to the wire.begin statement and change it's arguments to be the output lines of your sda and scl ports respectively.
Upload the program to the arduino 
PYTHON
Open the Magnetometer_readings.py since you will need it to query the serial port
In  Magnetometer_readings.py , replace basic_test.txt with a file name that you would like to save to.
Change the argument of serial.Serial to the name of the port that arduino is connected to.
Follow the instructions in the python program to configure as you like. By default the program reads from 3 probes per reading.
Start the python program and you should begin having the file read data and you are all set
