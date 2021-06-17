# 116117-Terminbot
Termin und Code Bot für den 116117 Impfterminservice. Einfache Python/Selenium Browser Automation

# Installation

Python 3.8 installieren

pip install selenium

chromedriver.exe zum PATH hinzufügen
Dafür in Windows Umgebungsvariablen suchen und dort Umgebungsvariablen unten rechts den Pfad zur exe hinzufügen
Der Pfad für den chromedriver muss momentan noch manuell im Code (Zeile 92 / 63)

# Code suchen
python tracker_Code.py -p DEINE_PLZ -b DEIN_GEBURTSTAG_TTMMYYYY

Um das Programm einfach zu starten oder mehrere Postleitzahlen abzusuchen, den codestarter.bat anpassen und nutzen.

Wenn das Programm piept, hat es einen Code gefunden. Nun müssen noch einige Daten eingegeben werden.

# Termin suchen
In Zeile 18 und 19 die Postleitzahl und den zuvor erhaltenen Code eingeben

!Der Code kann nur bei der Postleitzahl genutzt werden, bei der der Code erhalten wurde.

Wenn das Programm piept, bleiben 10 Minuten, um alle Daten einzugeben und den Termin zu bestätigen
