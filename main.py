from aufgabe import Aufgabe
from lernplan import Lernplan
from nutzer import Nutzer

def main():


    plan = Lernplan()


    wochenplan = plan.tage_planen()

    for tag, aufgaben in wochenplan.items():
        print(f"\n📅 {tag}:")
        for eintrag in aufgaben:
            print(f"  ➤ {eintrag}")

if __name__ == "__main__":
    main()
