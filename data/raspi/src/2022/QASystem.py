from MTTF import MTTFCalculator
from WestenDigitalRuleChecker import WesternDigitalRuleChecker
from Lights import Lights

class QASystem:

    def __init__(self):
        self.datapoints = []
        self.measured_value = 0
        # TODO Rufe den Konstruktor von MTTFCalculator (s. Datei MTTF) 
        # auf und speichere das Objekt in der Instanzvariable 
        # "self.mttf_calculator". Tipp: Konstruktoren werden mit "Klassenname()" aufgerufen. 
        # Ein Beispiel ist die Definition von "self.rule_checker" weiter unten.
        self.mttf_calculator = MTTFCalculator()

        self.estimated_value = self.ask_for_estimated_value()
        # TODO Rufe die von dir erstelle Methode auf, die nach der Standardabweichung fragt und 
        # speichere das Ergebnis in "self.standard_deviation". 
        # Tipp: Schau dir die Definition vom Erwartungswert ("estimated_value") an.
        self.standard_deviation = self.ask_for_stddev_value()

        self.rule_checker = WesternDigitalRuleChecker(self.estimated_value, self.standard_deviation)
        self.lights = Lights(17,27,22)

    def ask_for_estimated_value(self):
        """Asks for the estimated value and returns the user input"""
        # TODO Erstelle eine Eingabeaufforderung die nach dem Erwartungswert fragt
        # und gebe diesen zurueck. Achte darauf, dass das Ergebnis eine Gleitkommazahl ist. 
        # Das "pass" kann hier geloscht werden, wenn du deinen Code einfuegst.
        ret = float(input("Erwartungswert: "))
        return ret 

    # TODO Erstelle eine Methode, die den Nutzer um die Standardabweichung bittet
    # und diese als Gleitkommazahl zurueckgibt. 
    # Tipp: Schau dir die Definition von der ask_for_estimated_value-Funktion an.
    def ask_for_stddev_value():
        ret = float(input("Standardabweichung: "))
        return ret 


    def handle_input(self, value):
        """Wird aufgerufen, wenn ein neuer Messpunkt eingegeben wurde"""
        self.measured_value = value
        self.datapoints.append(self.measured_value)

        if(not self.rule_checker.check_rule_1(self.datapoints)):
            print("Rule 1 failed")
            # TODO Wenn diese Regel nicht eingehalten wird, ist das Werkstueck nicht nutzbar. 
            # Zeige dies mit der roten Lampe an.

            self.handle_error()
        elif(not self.rule_checker.check_rule_2(self.datapoints)):
            print("Rule 2 failed")
            self.handle_error()
        elif(not self.rule_checker.check_rule_3(self.datapoints)):
            print("Rule 3 failed")
            self.handle_error()
        # TODO Vervollstaendige die if-Abfrage um einen Test fuer die 4. Regel.



        else:
            # Datapoint is good
            self.lights.turn_green_light_on()

    def handle_error(self):
        """Diese Methode wird aufgerufen, wenn ein Fehler festgestellt wurde."""
        # TODO Stelle sicher, dass die Lampen in der richtigen Konfiguration leuchten.
        # Welche Lampen sind evenutell noch auszuschalten, welche eventuell anzuschalten?


        # TODO Berechne den alten MTTF

        # TODO Haenge die Anzahl der erfolgreich produzierten Stuecke an 
        # die failures Liste (mttf-Objekt) an.

        # TODO Berechne die neue MTTF.

        self.mttf_calculator.write_to_file()
        
        # TODO Gebe die alte und neue MTTF ueber die Konsole aus.

        self.datapoints = []
        self.measured_value = 0
        
        # TODO Frage den Nutzer, ob die Produktion fortgesetzt werden soll. 
        # Wenn ja, soll die Ampel entsprechend zurueckgesetzt werden. 
        # Wenn nein, soll der Nutzer wieder gefragt werden. 
        # Tipp: "while(true):" erstellt eine Endlosschleife. 
        # Die Ausfuehrung einer Schleife kann mit dem Befehl "break" beendet werden.
        while (True):
            if(eingabe == "ja"):
                self.lights.turn_lights_off()




if __name__=='__main__':
    qaSystem = QASystem()
    while(True):
        measured_value = float(input("Datapoint: "))
        qaSystem.handle_input(measured_value)