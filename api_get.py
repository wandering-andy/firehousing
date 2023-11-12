import sqlite3
from fastapi import FastAPI

app = FastAPI()

@app.get('/regions')
def get_regions():
    conn = sqlite3.connect('fs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Region")
    regions = cursor.fetchall()

    conn.close()

    return regions

@app.get('/forests')
def get_forests():
    conn = sqlite3.connect('fs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Forest")
    forests = cursor.fetchall()

    conn.close()

    return forests

@app.get('/districts')
def get_districts():
    conn = sqlite3.connect('fs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM District")
    districts = cursor.fetchall()

    conn.close()

    return districts

@app.get('/stations')
def get_stations():
    conn = sqlite3.connect('fs.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Station")
    stations = cursor.fetchall()

    conn.close()

    return stations