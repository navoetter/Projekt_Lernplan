class Nutzer:
    def __init__(self, name):
        self.name = name
        self.verfuegbare_zeiten = {}  # z. B. {"Montag": 2, "Dienstag": 1}

    def lernzeit_setzen(self, tag, stunden):
        self.verfuegbare_zeiten[tag] = stunden

    def anzeigen(self):
        print(f"Lernzeiten von {self.name}:")
        for tag, zeit in self.verfuegbare_zeiten.items():
            print(f"{tag}: {zeit} Stunden verfügbar")
