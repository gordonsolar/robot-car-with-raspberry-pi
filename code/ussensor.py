#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:14:59 2019

@author: tom
"""
import RPi.GPIO as GPIO
import asyncio
import time



class ultrasonic_sensor():
    def __init__(self, trigger_pin = 18, echo_pin = 25):
        GPIO.setmode(GPIO.BCM)
        #set GPIO Pins
        self.GPIO_TRIGGER = trigger_pin
        self.GPIO_ECHO = echo_pin
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        self.obj_distance = 999
        self.power_on = True

    async def determine_obj_distance(self):
        while self.power_on:
            # set Trigger to HIGH
            GPIO.output(self.GPIO_TRIGGER, True)
            # set Trigger after 0.01ms to LOW
            time.sleep(0.00001)
            GPIO.output(self.GPIO_TRIGGER, False)
            StartTime = time.time()
            StopTime = time.time()
            # save StartTime
            while GPIO.input(self.GPIO_ECHO) == 0:
                 StartTime = time.time()
            # save time of arrival
            while GPIO.input(self.GPIO_ECHO) == 1:
                StopTime = time.time()
            # time difference between start and arrival
            TimeElapsed = StopTime - StartTime
            # multiply with the sonic speed (34300 cm/s)
            # and divide by 2, because there and back
            self.obj_distance = (TimeElapsed * 34300) / 2
            await asyncio.sleep(0.2)




if __name__ == "__main__":

    async def test():
        run = 0
        while True:
            print("distance to next object is = ", distance_sensor.obj_distance)
            run += 1
            if run > 10:
                distance_sensor.power_on = False
                break
            await asyncio.sleep(0.5)

    GPIO.setmode(GPIO.BCM)
    distance_sensor = ultrasonic_sensor(trigger_pin = 18, echo_pin = 25)
    futures = [distance_sensor.determine_obj_distance(), test()]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(futures))
    loop.close()
    GPIO.cleanup()
