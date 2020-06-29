import TestRPiGPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class LED (object):
    ''' LED - Steuerungs - Klasse '''

    def __init__(self, pin, name):
        self.pin = pin
        self.name = name
        self.status = 0
        GPIO.setup(self.pin, GPIO.OUT)

    def turnLEDOn(self):
        self.status = 1
        print("ON")
        GPIO.output(self.pin, 1)

    def turnLEDOff(self):
        self.status = 0
        print("OFF")
        GPIO.output(self.pin, 0)

    def blinkLED(self, count):
        for b in range(count):
            self.turnLEDOn()
            time.sleep(0.25)
            self.turnLEDOff()
            time.sleep(0.25)


ledRot = LED(12, "rot")
ledRot.turnLEDOn()
time.sleep(1)
ledRot.blinkLED(10)
