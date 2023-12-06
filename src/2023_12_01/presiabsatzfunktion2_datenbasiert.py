import matplotlib.pyplot as plt
import numpy as np

def preisabsatzfunktion(preis):
    # Lineare Preisabsatzfunktion: Menge = m * Preis + b
    m = -0.5  # Steigung der Funktion
    b = 100   # y-Achsenabschnitt
    
    menge = m * preis + b
    return max(0, menge)  # Menge kann nicht negativ sein

# Preise im Bereich von 0 bis 200
preisbereich = np.arange(0, 201, 10)

# Erzeuge Daten mit zufälligem Rauschen
np.random.seed(42)  # Für Reproduzierbarkeit
rauschen = np.random.normal(0, 30, len(preisbereich))
mengen = [preisabsatzfunktion(preis) + r for preis, r in zip(preisbereich, rauschen)]

# Plot der Preisabsatzfunktion mit Rauschen
plt.plot(preisbereich, mengen, 'o', label='Daten mit Rauschen')
plt.xlabel('Preis')
plt.ylabel('Menge')
plt.title('Preisabsatzfunktion mit Rauschen')
plt.legend()
plt.grid(True)
plt.show()
