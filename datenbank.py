import mysql.connector
from datetime import datetime

class Datenbank:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="lernplan_db"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
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

    def aufgabe_speichern(self, fach, beschreibung, faelligkeit, prioritaet):
        try:
            faelligkeit_date = datetime.strptime(faelligkeit, "%d.%m.%Y").date()
        except ValueError:
            print("Falsches Datumsformat, bitte 'TT.MM.JJJJ' verwenden.")
            return

        self.cursor.execute("""
            INSERT INTO aufgaben (fach, beschreibung, faelligkeit, prioritaet)
            VALUES (%s, %s, %s, %s)
        """, (fach, beschreibung, faelligkeit_date, prioritaet))
        self.conn.commit()

    def alle_aufgaben_laden(self):
        self.cursor.execute("""
            SELECT fach, beschreibung, DATE_FORMAT(faelligkeit, '%%d.%%m.%%Y') AS faelligkeit, prioritaet
            FROM aufgaben ORDER BY faelligkeit, prioritaet
        """)
        return self.cursor.fetchall()