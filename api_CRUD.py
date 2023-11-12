import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the models for request and response data
class Region(BaseModel):
    id: int
    name: str

class Forest(BaseModel):
    id: int
    name: str
    region_id: int

class District(BaseModel):
    id: int
    name: str
    forest_id: int

class Station(BaseModel):
    id: int
    name: str
    district_id: int

# Define the routes for CRUD operations

@app.get('/regions/{region_id}')
def get_region(region_id: int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Region WHERE id=?", (region_id,))
    region = cursor.fetchone()

    conn.close()

    if region is None:
        raise HTTPException(status_code=404, detail="Region not found")

    return Region(id=region[0], name=region[1])

@app.post('/regions')
def create_region(region: Region):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Region (id, name) VALUES (?, ?)", (region.id, region.name))
    conn.commit()

    conn.close()

    return region

@app.put('/regions/{region_id}')
def update_region(region_id: int, region: Region):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("UPDATE Region SET name=? WHERE id=?", (region.name, region_id))
    conn.commit()

    conn.close()

    return region

@app.delete('/regions/{region_id}')
def delete_region(region_id: int):
    conn = sqlite3.connect('mydatabase.db')
    cursor = conn.cursor()

    cursor.execute("DELETE FROM Region WHERE id=?", (region_id,))
    conn.commit()

    conn.close()

    return {"message": "Region deleted"}


# Similarly, add routes for forests, districts, and stations


if __name__ == '__main__':
    app.run()