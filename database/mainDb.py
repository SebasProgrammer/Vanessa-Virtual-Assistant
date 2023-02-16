import sqlite3
import sys

if __name__ == '__main__':

    try:
        conn = sqlite3.connect("../people_documents.db")
        # conn.execute('''DROP TABLE PERSONA''')
        # conn.execute('''DROP TABLE DOCUMENTO''')
        conn.execute(''' CREATE TABLE IF NOT EXISTS PERSONA (
                            id INTEGER PRIMARY KEY,
                            nombre VARCHAR(50) NOT NULL);''')

        conn.execute('''CREATE TABLE IF NOT EXISTS DOCUMENTO (
                            id INTEGER PRIMARY KEY,
                            nombre VARCHAR(50) NOT NULL,
                            foto BLOB NOT NULL,
                            fecha datetime default current_timestamp,
                            persona_id INTEGER NOT NULL,
                            FOREIGN KEY(persona_id) REFERENCES PERSONA(id))
                            ;''')

        conn.commit()
        conn.close()
    except Exception as error:
        print(error)
