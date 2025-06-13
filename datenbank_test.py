from datenbank import Datenbank

db = Datenbank()
try:
    db.aufgabe_speichern("Chemie", "SMÜ", "12.06.2025", 2)
    print("Aufgabe erfolgreich gespeichert.")
except Exception as e:
    print("Fehler:", e)