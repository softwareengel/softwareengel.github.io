''' LED - Vorlage V.0.1 2022 VE '''
# import RPi.GPIO as GPIO # Livesystem RasPi
import TestRPiGPIO as GPIO # testsystem PC
from time import sleep

# hier pins aktivieren 

class LED (object):
    def __init__(self, pin):
        # pin in objekt der klasse merken 
        # setup pin als out 
        pass
    def turnOn(self):
        # pin dieses objekts output aktivieren 
        pass 
    def turnOff(self):
        # pin dieses objekts output deaktivieren 
        pass 

    def blink(self, count):
        # Scheife mit der Anzahl des Parameters cout durchlaufen 
        # bei jedem Durchlauf: diese led an, warten, led aus 
        pass

# Testen der Klasse 

# Legen sie ein Objekt Led an mit der Pinnummer 

# Lassen sie diese led 5 x blinken 