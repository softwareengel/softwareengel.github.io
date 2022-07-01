"""
An dieser Datei sollte nichts veraendert werden!
"""

BOARD = "board"
BCM = "bcm"
OUT = "out"
IN = "in"
LOW = 0
HIGH = 1

def output(pin,value):
    if value == 1:
        status = "on"
    else:
        status = "off"

    if pin == 17:
        print("green", status)
    elif pin == 27:
        print("yellow", status)
    elif pin == 22:
        print("red", status)

def setmode(mode):
    print (mode)

def setup(pin,value):
    if value == 1:
        status = "on"
    else:
        status = "off"

    if pin == 17:
        print("green", status)
    elif pin == 27:
        print("yellow", status)
    elif pin == 22:
        print("red", status)

def cleanup():
    print ("clean-up")

#End