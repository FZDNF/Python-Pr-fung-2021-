# Mietwohnungen 2016 – Deskriptive Statistik, Korrelation & Regression (Prüfungsleistung)

Dieses Repository enthält eine originale Prüfungsleistung aus meinem Studium.  
Ziel der Aufgabe war es, einen bereitgestellten Datensatz zu Mietwohnungen (CSV) in Python einzulesen, deskriptiv auszuwerten und einfache Zusammenhänge statistisch zu untersuchen.

## Inhalte (Aufgabenübersicht)

1. **Datenimport & Überblick**
   - Einlesen der CSV-Datei (`07-Mietwohnungen2016.csv`) mit `pandas`
   - Ausgabe der ersten Zeilen und Anzahl der Datensätze

2. **Deskriptive Statistik (metrische Variablen)**
   - Mittelwert und Standardabweichung für:
     - Zimmeranzahl
     - Fläche
     - Miete
   - Export der Ergebnistabelle in `Auswertungsergebnisse.txt`

3. **Häufigkeitsverteilungen (nominale Variablen)**
   - Balkendiagramme (horizontal) für:
     - Stadtteil
     - Ortskode
     - Lage

4. **Korrelationsanalyse (Pearson)**
   - Berechnung der Pearson-Korrelation zwischen **Fläche** und **Miete**
   - Einordnung der Stärke des Zusammenhangs anhand von Schwellenwerten

5. **Lineare Regression (einfaches Modell)**
   - Lineare Regression zwischen **Fläche** (x) und **Miete** (y) via `numpy.polyfit`
   - Scatterplot inkl. Regressionsgerade

## Verwendete Tools

- Python
- pandas, numpy
- matplotlib
- collections.Counter

## Ausführung

1. Stelle sicher, dass sich die Datei `07-Mietwohnungen2016.csv` im gleichen Verzeichnis wie das Skript befindet.
2. Script ausführen (z.B. über IDE oder Terminal).  
   - Es werden Konsolenausgaben erzeugt und mehrere Diagrammfenster geöffnet.
   - Zusätzlich wird eine Textdatei `Auswertungsergebnisse.txt` geschrieben.

## Hinweis

Die Analyse folgt dem Aufgabenformat der Prüfungsleistung und ist daher bewusst kompakt gehalten (keine umfassende Modellvalidierung oder Feature-Engineering).
