
'''
Instanziieren Sie auch für diese LED ein Objekt Ihrer LED Klasse.
Entwickeln Sie ein Programm, bei dem eine Zahl geraten werden soll, 
welche ein anderer Spieler zu Beginn eingibt. 
Wenn ein Spieler eine falsche Zahl eingibt, soll die eine LED so oft blinken, 
wie der Abstand der falschen zur richtigen Zahl ist.
Gibt der Spieler die richtige Zahl ein, soll die andere LED so oft blinken wie die Zahl groß ist.
Erweiterung:
Merken sie sich den Abstand von eingabeZahl zur zu ratenden Zahl in einer Liste mit dem Namen abstandListe. 
Geben sie jeweils den aktuellen Abstand und den vorherigen Anstand aus 
Bei Eingabe der richtigen zahl berechnen sie den Mittelwert von den Werten der abstandListe und geben den Mittelwert und alle Elemente aus

'''

from led import LED
led1 = LED(12, "eineLed")
led2 = LED(14, "andereLed")

def calc_mittelwert(abstandListe):
    sum = 0
    for x in abstandListe:
        sum += x
    mittelwert = sum / len(abstandListe)
    return mittelwert

# Eingabe rateZahl
zahl = int(input("zu erratende ganzzahlige Zahl eingeben:"))
rateende = 0
while (not rateende):
    abstandListe = []
    print("Bitte Raten: ")
    rateversuch = int(input())
    if zahl == rateversuch:
        # Geraten:          
        led2.blinkLED(zahl)
        rateende = 1
        mittelwert = calc_mittelwert(abstandListe)
        print (mittelwert, abstandListe)
    else:
        abstand = abs(zahl-rateversuch)
        led1.blinkLED(abstand)
        if (len(abstandListe) > 0):
            print(abstand, abstandListe[-1])
        # abstandListe += abstand,
        abstandListe.append(abstand)
