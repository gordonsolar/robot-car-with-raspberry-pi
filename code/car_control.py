#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:14:59 2019

@author: tom
"""
import RPi.GPIO as GPIO
import asyncio
import gamepad
import ussensor
import motor_control

async def car_control():
    car_break = 1
    while True:
        #stop if x is pressed
        if remote_control.button_x:
            remote_control.power_on = False
            remote_control.erase_rumble()
            distance_sensor.power_on = False
            car_motor_control.stop()
            GPIO.cleanup()
            break
        # rumble if distance < 20 and stop the car
        if (distance_sensor.obj_distance < 10) and (car_break > 0):
            remote_control.rumble_effect = 2
            car_break = 0
        elif (distance_sensor.obj_distance < 30) and (distance_sensor.obj_distance > 10):
            remote_control.rumble_effect = 1
            car_break = 0.5
        elif distance_sensor.obj_distance > 30:
            remote_control.rumble_effect = 0
            car_break = 1
        # set speed and direction
        if (remote_control.trigger_right > 1e-3) and (remote_control.trigger_left < 1e-3):
            speed = remote_control.trigger_right * car_break
        elif (remote_control.trigger_right < 1e-3) and (remote_control.trigger_left > 1e-3):
            speed = -1 * remote_control.trigger_left
        else:
            speed = 0
        direction = remote_control.joystick_left_x
        car_motor_control.set_speed_direction(speed,direction)
        await asyncio.sleep(0)


remote_control = gamepad.gamepad(file = '/dev/input/event0')
GPIO.setmode(GPIO.BCM)
distance_sensor = ussensor.ultrasonic_sensor(trigger_pin = 18, echo_pin = 25)
car_motor_control = motor_control.motor_control()

futures = [remote_control.read_gamepad_input(), remote_control.rumble(), distance_sensor.determine_obj_distance(), car_control()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(futures))
loop.close()
