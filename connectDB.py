import sqlite3
import sys

if __name__ == '__main__':
    record = sys.argv[1]
    conection = sqlite3.connect("Database.db")
    cursor = conection.cursor()
    # 1) Ya está creada la tabla INPUT
    # cursor.execute("CREATE TABLE INPUTS (Nombre VARCHAR(50))")

    # 2)Ingresar datos
    cursor.execute(f'INSERT INTO INPUTS VALUES("{record}")')
    conection.commit()
    conection.close()
