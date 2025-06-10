import mysql.connector
from datetime import datetime

class Datenbank:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="lernplan_db"
            )
            self.cursor = self.conn.cursor(dictionary=True)  # Damit werden Ergebnisse als Dictionary zurückgegeben
            self.create_table()
        except mysql.connector.Error as err:
            print(f"Fehler bei der Verbindung zur Datenbank: {err}")
            raise

    def __del__(self):
        """Schließt die Verbindung wenn das Objekt zerstört wird"""
        if hasattr(self, 'conn') and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()

    def create_table(self):
        try:
            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS aufgaben (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fach VARCHAR(100),
                    beschreibung TEXT,
                    faelligkeit DATE,
                    prioritaet INT
                )
            """)
            self.conn.commit()
        except mysql.connector.Error as err:
            print(f"Fehler beim Erstellen der Tabelle: {err}")
            raise

    def aufgabe_speichern(self, fach, beschreibung, faelligkeit, prioritaet):
        try:
            faelligkeit_date = datetime.strptime(faelligkeit, "%d.%m.%Y").date()
        except ValueError:
            print("Falsches Datumsformat, bitte 'TT.MM.JJJJ' verwenden.")
            return False

        try:
            self.cursor.execute("""
                INSERT INTO aufgaben (fach, beschreibung, faelligkeit, prioritaet)
                VALUES (%s, %s, %s, %s)
            """, (fach, beschreibung, faelligkeit_date, prioritaet))
            self.conn.commit()
            return True
        except mysql.connector.Error as err:
            print(f"Fehler beim Speichern der Aufgabe: {err}")
            return False

    def alle_aufgaben_laden(self):
        try:
            self.cursor.execute("""
                SELECT id, fach, beschreibung, 
                       DATE_FORMAT(faelligkeit, '%%d.%%m.%%Y') AS faelligkeit, 
                       prioritaet
                FROM aufgaben 
                ORDER BY faelligkeit, prioritaet
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Fehler beim Laden der Aufgaben: {err}")
            return []