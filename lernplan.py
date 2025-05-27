from datetime import timedelta, datetime

class Lernplan:
    def __init__(self):
        self.aufgaben = []

    def aufgabe_hinzufuegen(self, aufgabe):
        self.aufgaben.append(aufgabe)

    def tage_planen(self):
        heute = datetime.now()
        plan = {}
        for aufgabe in sorted(self.aufgaben, key=lambda a: (a.faelligkeit, a.prioritaet)):
            tag = heute.strftime("%A")
            if tag not in plan:
                plan[tag] = []
            plan[tag].append(aufgabe.anzeigen())
            heute += timedelta(days=1)
        return plan
