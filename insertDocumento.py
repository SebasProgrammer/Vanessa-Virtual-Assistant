import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    try:
        with open(filename, 'rb') as file:
            blobData = file.read()
        return blobData
    except Exception as error:
        print(error)
        return None

def saveImageToDb(img_path, name_doc):
    conn = sqlite3.connect("people_documents.db")
    conn.execute("PRAGMA foreign_keys = ON")
    # img_path = "C:\\pikachu.jpg"
    binary_img = convertToBinaryData(img_path)
    name_doc =  name_doc
    persona_id = 1

    insert_row ="INSERT INTO DOCUMENTO (nombre, foto, persona_id) \
              VALUES (? , ?, ?);"

    if binary_img is not None:
        row_tuple = (name_doc, binary_img, persona_id)
        conn.execute(insert_row, row_tuple)
        conn.commit()

    conn.close()
