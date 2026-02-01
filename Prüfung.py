"""
Prüfung.py



Von: Fabian Zaudig, Mat.Nr.:451211039

Hilfsmittel: Online-Recherche u. entsprechende Foren, Skripte aus den Vorlesungen

"""

# Aus Python Core-Library
from collections import Counter
# Pandas für den Import und die Formatierung von tabellarischen Daten
import pandas as pd
# Berechnungen und Array-Handling
import numpy as np
# Ausgabe von Diagrammen
import matplotlib.pyplot as plt


# Trennzeile zwischen Aufgaben
sep = "\n\n";


# Aufgabe 1)

# Einlesen der Daten aus einer Datei
file_path = "07-Mietwohnungen2016.csv"
# Der Delimiter muss (richtig!) angegeben werden um die Spalten richtig zu trennen
data = pd.read_csv(file_path, delimiter=";")

# Ausgabe der Aufgabe
print("\nAufgabe 1)\n")

# Augabe der ersten 10 Zeilen
print(data.head(10))

# Ausgabe der Anzahl der Datensätze, "f" als Befehl, um tatsächlichen Wert zu erhalten trotz ""-Eingabe
print(f"Anzahl der Datensätze: {data.count(0)[0]}")
print(sep)


# Aufgabe 2)

# Kolumnen bestimmen für die metrischen Merkmale Zimmeranzahl, Fläche und Miete
metric_columns = ["Zimmeranzahl", "Fläche", "Miete"]

# Pandas Dict für Ausgabe und Datei
metric_results = { "Merkmal":[], "Mittelwert":[], "Standardabweichung":[] }

# Für jede Statistik-Spalte...
for col in metric_columns:
    # alle Werte einer Spalte als Float in ein Array schreiben
    col_arr = np.array(data[col], dtype = float)

    # den Namen des Merkmals
    metric_name = col

    # den Mittelwert
    metric_mw = round(np.mean(col_arr), 2)

    # die Standardabweichung herausfinden
    metric_std = round(np.std(col_arr), 2)

    # un dem Table hinzufügen
    metric_results["Merkmal"].append(metric_name)
    metric_results["Mittelwert"].append(metric_mw)
    metric_results["Standardabweichung"].append(metric_std)

# Dataframe aus Ergebnissen erzeugen und in einen String wandeln
metric_table = f"{pd.DataFrame(data=metric_results)}"

# Ausgabe der Aufgabe
print("Aufgabe 2)\n")

# Ausgabe auf Bildschirm
print(metric_table)
print(sep)

# Scheiben der Ergebnisse in eine Datei
metric_file = "Auswertungsergebnisse.txt"
with open(metric_file, 'w') as fo:
    fo.write(metric_table)


# Aufgabe 3

# Spalten für die nominalen Werte Stadtteil, Ortskode, Lage
nominal_columns = ["Stadtteil", "Ortskode", "Lage"]

# pyplot zurücksetzen
plt.rcdefaults()

# Figur mit einer Reihen und Variablen Spalten, Größe anpassen, "subplot" als Befehl, um Diagramme nebeneinander anzeigen zu lassen
fig, axs = plt.subplots(1, len(nominal_columns), figsize=(12, 8))

# Titel des Fensters anpassen
fig.canvas.manager.set_window_title('Aufgabe 3) Häufigkeitsverteilung nominaler Merkmale')

barcolors = ["green", "blue", "orange"]

# Wie oft kommt ein Wert in einer Spalte vor:
for i, col in enumerate(nominal_columns):
    # Eine Spalte der Daten als Liste speichern
    nominal_values = data[col]
    # collections.Counter liefert Häufigkeit von Werten zurück
    nominal_counter = Counter(nominal_values)

    # Bezeichner und Häufigkeit in Listen speichern
    nominal_counter_keys = []
    nominal_counter_values = []
    for key, val in nominal_counter.items():
        nominal_counter_keys.append(key)
        nominal_counter_values.append(val)

    # liste mit Indexes für die Y-Position
    y_pos = list(range(len(nominal_counter_keys)))
    # Balken zeichnen
    axs[i].barh(y_pos, nominal_counter_values, align='center',
            color=barcolors[i], ecolor='black')
    axs[i].set_yticks(y_pos)
    axs[i].set_yticklabels(nominal_counter_keys)
    axs[i].invert_yaxis()  # Labels von oben nach unten
    # Beschriftung hinzufügen
    axs[i].set_title(f"Verteilung nach {col}")
    axs[i].set_xlabel('Anzahl Wohnungen')

# Darstellen der Diagramme in einem neuen Fenster
plt.show()


# Aufgabe 4

# 2 geeignete Spalten auswählen
pearson_key_a = "Fläche"
pearson_key_b = "Miete"

# Und deren Werte in Arrays schreiben
pearson_a = np.array(data[pearson_key_a], dtype = float)
pearson_b = np.array(data[pearson_key_b], dtype = float)

# Mit numpy.corrcoef den Korrelationskoeffizienten nach Pearson berechnen
# und aus der Ergebnis-Matrix den relevanten Wert ziehen
pearson_corr = np.corrcoef(pearson_a, pearson_b)[0][1]

# Ausgabe der Aufgabe
print("Aufgabe 4)\n")
print(f"Der Korrelationskoeffizient zwischen {pearson_key_a} und {pearson_key_b} beträgt {pearson_corr}.")
if abs(pearson_corr) >= 0.8:
    print("Es handelt sich hierbei um einen starken Zusammenhang")
elif abs(pearson_corr) >= 0.6:
    print("Es handelt sich hierbei um einen mittleren Zusammenhang")
elif abs(pearson_corr) == 0.0:
    print("Ein Zusammenhang ist nicht erkennbar")
else:
    print("Es handelt sich hierbei um einen schwachen Zusammenhang")


# Aufgabe 5

# 2 geeignete Spalten auswählen und beschreiben
regres_key_x = "Fläche"
regres_label_x = "Fläche in qm"

regres_key_y = "Miete"
regres_label_y = "Miete in €"

# Und deren Werte in Arrays schreiben
regres_x = np.array(data[regres_key_x], dtype = float)
regres_y = np.array(data[regres_key_y], dtype = float)

# Modell der linearen Regression mittels polyfit herstellen
regres_model = np.polyfit(regres_x, regres_y, 1)
# Funktion auf Basis des Models erzeugen
regres_predict = np.poly1d(regres_model)

# Maximalwert auf der x-Achse finden und zu Integer wandeln
regres_max_x = int(np.amax(regres_x)) + 1

# X-Werte für Regressionsgerade generieren
regres_line_x = list(range(regres_max_x))

# y-Werte für Regressionsgerade berechnen
regres_line_y = regres_predict(regres_line_x)

# pyplot zurücksetzen
plt.rcdefaults()

# Figur- Größe anpassen
fig, axs = plt.subplots(figsize=(12, 8))

# Titel des Fensters anpassen
fig.canvas.manager.set_window_title("Aufgabe 5) Lineare Regression zweier Merkmale")

axs.set_title(f"Lineare Regression zwischen {regres_key_x} und {regres_key_y}")
axs.set_xlabel(regres_label_x)
axs.set_ylabel(regres_label_y)

# Datenpunkte plotten
axs.scatter(regres_x, regres_y, alpha=0.3)

# Regressionslinie zeichnen
axs.plot(regres_line_x, regres_line_y, color="red")

# Darstellen des Scanner Plot in einem neuen Fenster
plt.show()
