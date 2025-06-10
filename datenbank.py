import mysql.connector

class Datenbank:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="",
            password="",
            database="lernplan_db"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS aufgaben (
                id INT AUTO_INCREMENT PRIMARY KEY,
                fach VARCHAR(255) NOT NULL,
                beschreibung TEXT NOT NULL,
                faelligkeit DATE NOT NULL,
                prioritaet INT NOT NULL
            )
        """)
        self.conn.commit()

    def aufgabe_speichern(self, fach, beschreibung, faelligkeit, prioritaet):
        self.cursor.execute("""
            INSERT INTO aufgaben (fach, beschreibung, faelligkeit, prioritaet)
            VALUES (%s, %s, STR_TO_DATE(%s, '%%d.%%m.%%Y'), %s)
        """, (fach, beschreibung, faelligkeit, prioritaet))
        self.conn.commit()

    def alle_aufgaben_laden(self):
        self.cursor.execute("""
            SELECT fach, beschreibung, DATE_FORMAT(faelligkeit, '%%d.%%m.%%Y'), prioritaet
            FROM aufgaben ORDER BY faelligkeit, prioritaet
        """)
        return self.cursor.fetchall()
