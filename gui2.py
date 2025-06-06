import tkinter as tk
from tkinter import messagebox
from tkinter import ttk  # für coolere Widgets
from aufgabe import Aufgabe
from lernplan import Lernplan

class LernplanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Lernplan Manager")
        self.root.geometry("500x600")
        self.root.configure(bg="#975fb4")  # heller Hintergrund

        self.plan = Lernplan()

        # Hauptframe mit Padding und Rahmen
        main_frame = ttk.Frame(root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Überschrift
        titel = ttk.Label(main_frame, text="Lernplan Manager", font=("Helvetica", 20, "bold"))
        titel.pack(pady=10)

        # Eingabefelder in eigenem Rahmen
        input_frame = ttk.LabelFrame(main_frame, text="Neue Aufgabe hinzufügen", padding=10)
        input_frame.pack(fill=tk.X, pady=10)

        # Fach
        ttk.Label(input_frame, text="Fach:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.fach_entry = ttk.Entry(input_frame)
        self.fach_entry.grid(row=0, column=1, sticky=tk.EW, pady=5)

        # Beschreibung
        ttk.Label(input_frame, text="Beschreibung:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.beschreibung_entry = ttk.Entry(input_frame)
        self.beschreibung_entry.grid(row=1, column=1, sticky=tk.EW, pady=5)

        # Fälligkeitsdatum
        ttk.Label(input_frame, text="Fälligkeitsdatum (TT.MM.JJJJ):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.faelligkeit_entry = ttk.Entry(input_frame)
        self.faelligkeit_entry.grid(row=2, column=1, sticky=tk.EW, pady=5)

        # Priorität
        ttk.Label(input_frame, text="Priorität (1-3):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.prioritaet_entry = ttk.Entry(input_frame)
        self.prioritaet_entry.grid(row=3, column=1, sticky=tk.EW, pady=5)

        # Eingabespalten gleich breit machen
        input_frame.columnconfigure(1, weight=1)

        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        self.btn_add = ttk.Button(button_frame, text="Aufgabe hinzufügen", command=self.aufgabe_hinzufuegen)
        self.btn_add.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0,5))

        self.btn_show = ttk.Button(button_frame, text="Lernplan anzeigen", command=self.lernplan_anzeigen)
        self.btn_show.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(5,0))

        # Textfeld mit Scrollbar für Ausgabe
        ausgabe_frame = ttk.LabelFrame(main_frame, text="Lernplan")
        ausgabe_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        self.ausgabe = tk.Text(ausgabe_frame, height=15, wrap=tk.WORD)
        self.ausgabe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,5), pady=5)

        scrollbar = ttk.Scrollbar(ausgabe_frame, orient=tk.VERTICAL, command=self.ausgabe.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.ausgabe.config(yscrollcommand=scrollbar.set)

    def aufgabe_hinzufuegen(self):
        fach = self.fach_entry.get().strip()
        beschreibung = self.beschreibung_entry.get().strip()
        faelligkeit = self.faelligkeit_entry.get().strip()
        prioritaet = self.prioritaet_entry.get().strip()

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
