# Importieren der benötigten Bibliotheken
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Annahme: Sie haben einen Datensatz mit relevanten Merkmalen (Features) und der Zielvariable (Kündigungsstatus)
# Beispiel-Datensatz (ersetzen Sie dies durch Ihren eigenen Datensatz):
data = {
    'Alter': [25, 30, 35, 40, 45],
    'Zahlungshistorie': [1, 2, 1, 3, 2],
    'Dauer_des_Mietverhältnisses': [2, 4, 3, 5, 2],
    'Einkommen': [50000, 60000, 75000, 80000, 70000],
    'Kündigungsstatus': [0, 1, 0, 1, 0]  # 0: Nicht gekündigt, 1: Gekündigt
}

# Erstellen Sie einen DataFrame aus dem Datensatz
df = pd.DataFrame(data)

# Aufteilen in Features (X) und Zielvariable (y)
X = df.drop('Kündigungsstatus', axis=1)
y = df['Kündigungsstatus']

# Aufteilen in Trainings- und Testdaten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialisieren des Random Forest Klassifikators
model = RandomForestClassifier(random_state=42)

# Trainieren des Modells
model.fit(X_train, y_train)

# Vorhersagen auf den Testdaten
predictions = model.predict(X_test)

# Auswertung des Modells
accuracy = accuracy_score(y_test, predictions)
report = classification_report(y_test, predictions)

# Ausgabe der Ergebnisse
print(f'Genauigkeit: {accuracy}')
print('Klassifikationsbericht:')
print(report)
# Importieren der benötigten Bibliotheken
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Visualisierung des Entscheidungsbaums
plt.figure(figsize=(10, 8))
plot_tree(model, feature_names=X.columns, class_names=['Nicht gekündigt', 'Gekündigt'], filled=True, rounded=True)
plt.show()
