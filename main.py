from aufgabe import Aufgabe
from lernplan import Lernplan
from nutzer import Nutzer

def main():
    nutzer = Nutzer("Max")
    nutzer.lernzeit_setzen("Montag", 2)
    nutzer.lernzeit_setzen("Dienstag", 1)

    plan = Lernplan()

    a1 = Aufgabe("Mathe", "Kurvendiskussion lernen", "30.05.2025", 1)
    a2 = Aufgabe("Bio", "Zellaufbau zusammenfassen", "29.05.2025", 2)

    plan.aufgabe_hinzufuegen(a1)
    plan.aufgabe_hinzufuegen(a2)

    wochenplan = plan.tage_planen()

    for tag, aufgaben in wochenplan.items():
        print(f"\n📅 {tag}:")
        for eintrag in aufgaben:
            print(f"  ➤ {eintrag}")

if __name__ == "__main__":
    main()
