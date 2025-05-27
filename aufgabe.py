from datetime import datetime

class Aufgabe:
    def __init__(self, fach, beschreibung, faelligkeit, prioritaet):
        self.fach = fach
        self.beschreibung = beschreibung
        self.faelligkeit = datetime.strptime(faelligkeit, "%d.%m.%Y")
        self.prioritaet = prioritaet  # z. B. 1 = hoch, 3 = niedrig

    def ist_faellig(self):
        return datetime.now() > self.faelligkeit

    def anzeigen(self):
        return f"[{self.fach}] {self.beschreibung} - fällig bis {self.faelligkeit.strftime('%d.%m.%Y')} (Priorität {self.prioritaet})"
