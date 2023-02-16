import sqlite3
from flask import Flask, render_template, url_for, g, request, jsonify, redirect, send_from_directory
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.oracle import BLOB
import markdown
import time

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

app = Flask(__name__, static_folder = "static")

@app.route('/documents', methods = ["POST", "GET"])
def documents():
    img_path=""
    try:
        if request.method == "POST":
            name = request.form.get("name_doc")
            print(name)
            if name != None:
                conn = sqlite3.connect("people_documents.db")
                cursor = conn.cursor()
                query = f"SELECT * from DOCUMENTO where nombre='{name}'"
                cursor.execute(query)
                conn.commit()
                result = cursor.fetchall()[0][2]
                img_path = "static/HOLA.png"
                time.sleep(10)
                write_file(result, img_path)
                cursor.close()
                conn.close()
                return render_template("index.html", documents=img_path)
    except Exception as error:
        print(error)

    return render_template("index.html")

@app.route('/', methods=['GET'])
def bghome():
    return send_from_directory("static", "dni.png")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)