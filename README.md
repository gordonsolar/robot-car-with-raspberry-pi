# Robot car with raspberry pi
Python modules to control a robot car consisting of a 2-motors-3-wheel-platform, raspberry pi 3, motor control IC L293D, xbox controller as remote control and an ultrasonic distance sensor.

The software allows to controll direction and speed of the car. Asyncronuously the distance of the objects in front of the car is measured with the ultrasonic sensor. When the distance drops below a certain threshold, the xbox controller starts to rumble. Below the critical distance the car stops.

## used HW componentes are:
1. Raspberry Pi Modell 3B with necessary components like power supply and memory card
2. Robot Car Chassis Kit with 3 wheels
3. Motor controller IC L293D
4. Ultra sonic distance sensor modul HC-SR04
5. xbox game controller bluetooth 
6. IC sockets, resistor 1 and 2 kOhm, female connector strip and cable

## used SW components are:
1. python3.6
2. python evdev module
3. python RPi.GPIO module 
4. python asyncio module
5. xpadneo driver for the xbox controller

Installation, detailed description and use see Wiki page.
Have fun!
