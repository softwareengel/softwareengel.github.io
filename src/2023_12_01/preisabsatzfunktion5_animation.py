import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

def preisabsatzfunktion_linear(preis):
    m = -0.5
    b = 100
    menge = m * preis + b
    return max(0, menge)

def preisabsatzfunktion_quadratic(preis):
    a = -0.005
    b = 1.5
    c = 50
    menge = a * preis**2 + b * preis + c
    return max(0, menge)

def update(frame):
    plt.clf()

    preisbereich = np.arange(0, 201, 10)
    rauschen = np.random.normal(0, 30, len(preisbereich))
    
    ax1 = plt.subplot(121)
    ax1.plot(preisbereich, [preisabsatzfunktion_linear(p) + r for p, r in zip(preisbereich, rauschen)], 'o', label='Daten mit Rauschen')
    ax1.set_xlabel('Preis')
    ax1.set_ylabel('Menge')
    ax1.set_title('Lineare Preisabsatzfunktion')
    ax1.legend()
    ax1.grid(True)

    trendlinie_koeffizienten = np.polyfit(preisbereich, [preisabsatzfunktion_linear(p) + r for p, r in zip(preisbereich, rauschen)], 1)
    trendlinie = np.polyval(trendlinie_koeffizienten, preisbereich)
    ax1.plot(preisbereich, trendlinie, label='Trendlinie', color='red')
    ax1.legend()

    ax2 = plt.subplot(122)
    ax2.plot(preisbereich, [preisabsatzfunktion_quadratic(p) + r for p, r in zip(preisbereich, rauschen)], 'o', label='Daten mit Rauschen')
    ax2.set_xlabel('Preis')
    ax2.set_ylabel('Menge')
    ax2.set_title('Quadratische Preisabsatzfunktion')
    ax2.legend()
    ax2.grid(True)

    trendlinie_koeffizienten = np.polyfit(preisbereich, [preisabsatzfunktion_quadratic(p) + r for p, r in zip(preisbereich, rauschen)], 2)
    trendlinie = np.polyval(trendlinie_koeffizienten, preisbereich)
    ax2.plot(preisbereich, trendlinie, label='Trendlinie', color='red')
    ax2.legend()

# Erstelle Animation
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
animation = FuncAnimation(fig, update, frames=range(50), interval=500)

# Speichere Video (optional)
# animation.save('preisabsatz_animation.mp4', writer='ffmpeg', fps=2)

plt.show()
