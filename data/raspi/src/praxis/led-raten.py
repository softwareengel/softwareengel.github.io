''' 
Instanziieren Sie auch für diese LED ein Objekt Ihrer LED Klasse.
Entwickeln Sie ein Programm, bei dem eine Zahl geraten werden soll, 
welche ein anderer Spieler zu Beginn eingibt. 
Wenn ein Spieler eine falsche Zahl eingibt, soll die eine LED so oft blinken, 
wie der Abstand der falschen zur richtigen Zahl ist.
Gibt der Spieler die richtige Zahl ein, soll die andere LED so oft blinken wie die Zahl groß ist.

'''

from led import LED
led1 = LED(12, "eineLed")
led2 = LED(14, "andereLed")

# Eingabe rateZahl
zahl  = int(input ("zu erratende ganzzahlige Zahl eingeben:"))
rateende = 0
while (not rateende):
    print ("Bitte Raten: ")
    rateversuch = int(input ())
    if zahl == rateversuch:
        # Geraten: 
        led2.blinkLED (zahl)
        rateende = 1
    else:
        anzalBlink = abs(zahl-rateversuch)
        led1.blinkLED(anzalBlink)


