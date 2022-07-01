# Übung Computergestützte Qualitätskontrollstation 

## Anwendungsfall
In eine Produktionskette soll eine Qualitätskontrollstation eingeführt werden. An dieser sollen Werkstücke
vermessen und die Messwerte in ein Kontrollsystem eingegeben werden. Dieses System soll die
eingegebenen Daten überprüfen und über ein Ampelsystem (Grün, Gelb, Rot) eine visuelle Rückmeldung
geben, ob das aktuell kontrollierte Werkstück die Qualitätsanforderungen erfüllt (grünes Licht
leuchtet) oder nicht (gelbes Licht leuchtet). Ein Messwert soll als zulässig gelten, wenn er sich innerhalb
von ±3 Standardabweichungen vom Erwartungswert befindet.
Um eine langfristige Qualitätsentwicklung beobachten zu können, sollen die Eingaben der Mitarbeiter
innerhalb des Systems gespeichert und gemäß den „Western Electric Rules“1 analysiert werden. Wird
eine Anomalie entdeckt, soll die Produktion unterbrochen werden, um Verbesserungsmaßnahmen
durchführen zu können. Das Ampelsystem soll dies durch das zusätzliche Leuchten der roten Lampe
anzeigen. Durch eine Eingabe in die Konsole der Qualitätskontrollstation soll eine Wiederaufnahme
der Arbeiten möglich sein. Ab hier soll eine neue Messreihe begonnen werden. Darüber hinaus soll die
MTTF (Mean Time to Failure) in erfolgreich produzierten Werkstücken bestimmt werden, um überprüfen
zu können, ob die Qualität des Produktionsprozesses zu- bzw. abnimmt. Diese soll bei jedem
Ausfall in der Konsole angezeigt werden und in eine Logdatei gespeichert werden.

## Technische Realisierung
Die Qualitätskontrollstation wird auf Basis eines Raspberry Pi realisiert, der die Eingaben durch ein
Konsolenfenster erhält. Die Ampel besteht aus drei Leuchtdioden, welche über den Raspberry Pi gesteuert
werden. Die zu entwickelnde Logik läuft als Python-Skript auf dem Raspberry Pi.
Die Messwerte sind einfache Zahlenwerte (floats), sodass man die entwickelte Lösung auf verschiedene
Messfälle anwenden kann. Um eine wiederverwendbare Lösung zu entwickeln, wird der Nutzer bei
dem Start des Skriptes aufgefordert, den Erwartungswert und die einfache Standardabweichung anzugeben.
Es wird von einer Normalverteilung der Messwerte ausgegangen.

## Aufgabe

1. Vervollständigen sie den gegebenen Code, um die oben beschriebenen Funktionen zu realisieren.

## Links 

http://en.wikipedia.org/wiki/Western_Electric_rules 