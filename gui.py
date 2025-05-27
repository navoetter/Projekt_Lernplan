import tkinter as tk
from tkinter import messagebox
from aufgabe import Aufgabe
from lernplan import Lernplan

class LernplanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lernplan Manager")

        self.plan = Lernplan()

        # Eingabefelder
        tk.Label(root, text="Fach:").grid(row=0, column=0)
        self.fach_entry = tk.Entry(root)
        self.fach_entry.grid(row=0, column=1)

        tk.Label(root, text="Beschreibung:").grid(row=1, column=0)
        self.beschreibung_entry = tk.Entry(root)
        self.beschreibung_entry.grid(row=1, column=1)

        tk.Label(root, text="Fälligkeitsdatum (TT.MM.JJJJ):").grid(row=2, column=0)
        self.faelligkeit_entry = tk.Entry(root)
        self.faelligkeit_entry.grid(row=2, column=1)

        tk.Label(root, text="Priorität (1-3):").grid(row=3, column=0)
        self.prioritaet_entry = tk.Entry(root)
        self.prioritaet_entry.grid(row=3, column=1)

        # Buttons
        tk.Button(root, text="Aufgabe hinzufügen", command=self.aufgabe_hinzufuegen).grid(row=4, column=0, columnspan=2)

        tk.Button(root, text="Lernplan anzeigen", command=self.lernplan_anzeigen).grid(row=5, column=0, columnspan=2)

        # Textfeld zur Anzeige
        self.ausgabe = tk.Text(root, width=50, height=15)
        self.ausgabe.grid(row=6, column=0, columnspan=2)

    def aufgabe_hinzufuegen(self):
        fach = self.fach_entry.get()
        beschreibung = self.beschreibung_entry.get()
        faelligkeit = self.faelligkeit_entry.get()
        prioritaet = self.prioritaet_entry.get()

        if not (fach and beschreibung and faelligkeit and prioritaet):
            messagebox.showwarning("Fehler", "Bitte alle Felder ausfüllen")
            return

        try:
            prioritaet = int(prioritaet)
            if prioritaet < 1 or prioritaet > 3:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Fehler", "Priorität muss eine Zahl zwischen 1 und 3 sein")
            return

        try:
            neue_aufgabe = Aufgabe(fach, beschreibung, faelligkeit, prioritaet)
        except Exception as e:
            messagebox.showerror("Fehler", f"Ungültiges Datum: {e}")
            return

        self.plan.aufgabe_hinzufuegen(neue_aufgabe)
        messagebox.showinfo("Erfolg", "Aufgabe hinzugefügt!")
        self.clear_entries()

    def clear_entries(self):
        self.fach_entry.delete(0, tk.END)
        self.beschreibung_entry.delete(0, tk.END)
        self.faelligkeit_entry.delete(0, tk.END)
        self.prioritaet_entry.delete(0, tk.END)

    def lernplan_anzeigen(self):
        plan = self.plan.tage_planen()
        self.ausgabe.delete(1.0, tk.END)
        for tag, aufgaben in plan.items():
            self.ausgabe.insert(tk.END, f"{tag}:\n")
            for a in aufgaben:
                self.ausgabe.insert(tk.END, f"  - {a}\n")
            self.ausgabe.insert(tk.END, "\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LernplanGUI(root)
    root.mainloop()
