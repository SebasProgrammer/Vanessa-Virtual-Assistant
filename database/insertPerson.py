import sqlite3
from photoToBinary import convertPhotoToBinary

conn = sqlite3.connect("../people_documents.db")
conn.execute("INSERT INTO PERSONA (nombre) VALUES ('sebastian')");
conn.commit()
conn.close()
