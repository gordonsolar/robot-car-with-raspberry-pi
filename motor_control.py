#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 23:14:59 2019

@author: tom
"""
import RPi.GPIO as GPIO

class Motor:

    def __init__(self, pinForward, pinBackward, pinControl):
        """ Initialize the motor with its control pins and start pulse-width
             modulation """
        self.pinForward = pinForward
        self.pinBackward = pinBackward
        self.pinControl = pinControl
        GPIO.setup(self.pinForward, GPIO.OUT)
        GPIO.setup(self.pinBackward, GPIO.OUT)
        GPIO.setup(self.pinControl, GPIO.OUT)
        self.pwm_forward = GPIO.PWM(self.pinForward, 20)
        self.pwm_backward = GPIO.PWM(self.pinBackward, 20)
        self.pwm_forward.start(0)
        self.pwm_backward.start(0)
        GPIO.output(self.pinControl,GPIO.HIGH)

    def forward(self, pwm):
        """ pinForward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_backward.ChangeDutyCycle(0)
        self.pwm_forward.ChangeDutyCycle(pwm)

    def backward(self, pwm):
        """ pinBackward is the forward Pin, so we change its duty
             cycle according to speed. """
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(pwm)

    def stop(self):
        """ Set the duty cycle of both control pins to zero to stop the motor. """
        self.pwm_forward.ChangeDutyCycle(0)
        self.pwm_backward.ChangeDutyCycle(0)

class motor_control():

    def __init__(self, m1_pinForward = 22, m1_pinBackward = 24, m1_pinControl = 4, m2_pinForward = 17, m2_pinBackward = 27, m2_pinControl = 23):
        GPIO.setmode(GPIO.BCM)
        self.motor_right = Motor(m1_pinForward, m1_pinBackward, m1_pinControl)
        self.motor_left = Motor(m2_pinForward, m2_pinBackward, m2_pinControl)

    def set_speed_direction(self, speed, direction):
        if direction >= 0:
            pwm_left = round(1 * speed * 100)
            pwm_right = round((1 - direction) * speed * 100)
        else:
            pwm_left = round((1 + direction) * speed * 100)
            pwm_right = round(1 * speed * 100)
        if speed >= 0:
            self.motor_left.forward(pwm_left)
            self.motor_right.forward(pwm_right)
        else:
            self.motor_left.backward(-1 * pwm_left)
            self.motor_right.backward(-1 * pwm_right)

    def stop(self):
        self.motor_left.stop()
        self.motor_right.stop()


if __name__ == "__main__":

    car_motor_control = motor_control()
    car_motor_control.set_speed_direction(1,0)
    car_motor_control.set_speed_direction(1,-0.5)
    car_motor_control.set_speed_direction(1,0.5)
    car_motor_control.stop()
    GPIO.cleanup()
