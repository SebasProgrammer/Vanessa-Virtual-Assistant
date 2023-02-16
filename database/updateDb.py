import sqlite3

conn = sqlite3.connect("../people_documents.db")

conn.execute("UPDATE PERSONA set nombre = 'sebastian' where id = 1")
conn.commit()
conn.close()