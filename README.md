# Robot car with raspberry pi
Python modules to control a robot car consisting of a 2-motors-3-wheel-platform, raspberry pi 3, motor control IC L293D, xbox controller as remote control and an ultrasonic distance sensor.

The software allows to controll direction and speed of the car. Asyncronuously the distance of the objects in front of the car is measured with the ultrasonic sensor. When the distance drops below a certain threshold, the xbox controller starts to rumble. Below the critical distance the car stops.

## used HW componentes are:
1. Raspberry Pi Modell 3B with necessary components like power supply and memory card
2. Robot Car Chassis Kit with 3 wheels
(e.g https://www.amazon.de/SainSmart-intelligente-Roboter-Auto-Fahrgestelle-Drehzahlgeber-Batterie-Chassis/dp/B072N7QNV9/ref=sr_1_12_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=raspberry+car&qid=1558157268&s=gateway&sr=8-12-spons&psc=1)
3. Motor controller IC L293D
(e.g. https://www.amazon.de/gp/product/B00K67WDB6/ref=ppx_yo_dt_b_asin_title_o01_s00?ie=UTF8&psc=1)
4. Ultra sonic distance sensor modul HC-SR04
(e.g. https://www.amazon.de/gp/product/B00BIZQWYE/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1)
5. xbox game controller bluetooth (e.g. https://www.amazon.de/Microsoft-218441-Wireless-Controller-schwarz/dp/B01L7PQBL8/ref=sxbs_sxwds-stvp?keywords=xbox-controller+microsoft+pc&pd_rd_i=B01L7PQBL8&pd_rd_r=54dbf868-a21b-4efb-b8c1-a988397eab9b&pd_rd_w=enx0K&pd_rd_wg=dVivq&pf_rd_p=6d84c7ba-ae72-4e53-b9a4-5df18ccb370e&pf_rd_r=HD8BH0VZQBDHBP1FNJDX&qid=1558157569&s=computers)
6. IC sockets, resistor 1 and 2 kOhm, female connector strip and cable

## used SW components are:
1. python3.6
2. python evdev module
3. python RPi.GPIO module 
4. python asyncio module
5. xpadneo driver for the xbox controller

Installation, detailed description and use see Wiki page.
Have fun!
