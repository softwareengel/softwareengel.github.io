import matplotlib.pyplot as plt
import numpy as np

def preisabsatzfunktion(preis):
    # Quadratische Preisabsatzfunktion: Menge = a * Preis^2 + b * Preis + c
    a = -0.005  # Quadratischer Koeffizient
    b = 1.5     # Linearer Koeffizient
    c = 50      # Konstante
    
    menge = a * preis**2 + b * preis + c
    return max(0, menge)  # Menge kann nicht negativ sein

# Preise im Bereich von 0 bis 200
preisbereich = np.arange(0, 201, 10)

# Erzeuge Daten mit zufälligem Rauschen
np.random.seed(42)  # Für Reproduzierbarkeit
rauschen = np.random.normal(0, 30, len(preisbereich))
mengen = [preisabsatzfunktion(preis) + r for preis, r in zip(preisbereich, rauschen)]

# Führe quadratische Regression durch, um die Trendlinie zu erhalten
trendlinie_koeffizienten = np.polyfit(preisbereich, mengen, 2)
trendlinie = np.polyval(trendlinie_koeffizienten, preisbereich)

# Plot der Preisabsatzfunktion mit Rauschen und quadratischer Trendlinie
plt.plot(preisbereich, mengen, 'o', label='Daten mit Rauschen')
plt.plot(preisbereich, trendlinie, label='Quadratische Trendlinie', color='red')
plt.xlabel('Preis')
plt.ylabel('Menge')
plt.title('Quadratische Preisabsatzfunktion mit Rauschen und Trendlinie')
plt.legend()
plt.grid(True)
plt.show()
