import sqlite3

conn = sqlite3.connect("../people_documents.db")

def writeTofile(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")

def readTofile(data, filename):
    with open(filename, 'r') as file:
        file.read(data)




cursor = conn.cursor()
query = "SELECT * from DOCUMENTO where nombre='pikachu'"
cursor.execute(query)
record = cursor.fetchall()
for row in record:
    id = row[0]
    name = row[1]
    foto = row[2]
    fecha = row[3]
    persona = row[4]
    print(id,name, foto, fecha, persona)
    img_save_path = "C:\\pythonProject3\\static\\" + name + ".jpg"
    writeTofile(foto, img_save_path)

cursor.close()

conn.close()