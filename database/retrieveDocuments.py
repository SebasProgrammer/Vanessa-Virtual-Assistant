import sqlite3

def showAllDocuments(name_table):
    conn = sqlite3.connect("people_documents.db")
    cursor = conn.cursor()
    query = f"SELECT * from {name_table} where persona_id=1"
    cursor.execute(query)
    names = list(map(lambda x: x[0], cursor.description))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result, names

