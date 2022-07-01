import csv
class MTTFCalculator:

    def __init__(self):
        self.failures = []
        self.read_from_file()

    def calculate_mttf(self):
        # TODO Berechne den Mittelwert der in "failures" gespeicherten Werte und gebe das Ergebnis zurueck. 
        # Tipp: Hierzu benoetigst du die "return"-Anweisung. 
        # Das pass kannst du loeschen, sobald du deinen Code schreibst.
        
        pass

    def write_to_file(self):
        """Hier wird die failures Liste in eine CSV Datei geschrieben"""
        logfile = open("logfile.csv", 'w', newline='')
        wr = csv.writer(logfile,dialect=csv.excel)
        wr.writerows([list(range(1,len(self.failures)+1)), self.failures])

    def read_from_file(self):
        """Hier wird zu beginn geschaut, ob es eine logfile gibt.
        Wenn ja, wird diese ausgelesen und die Werte in failures gespeichert"""
        try:
            logfile = open ("logfile.csv", "r")
            rows = list(csv.reader(logfile, dialect=csv.excel))
            if(len(rows)>1):
                for entry in rows[1]:
                    self.failures.append(int(entry))
        except:
            print("No Logfile Found")