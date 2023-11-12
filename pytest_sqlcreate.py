import sqlite3
from fastapi.testclient import TestClient
import pytest
from main import app

client = TestClient(app)

@pytest.fixture
def test_db():
    # Connect to an in-memory database for testing
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    # Create the tables and insert some test data
    cursor.execute('''
        CREATE TABLE Region (
            id INTEGER PRIMARY KEY,
            name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE Forest (
            id INTEGER PRIMARY KEY,
            name TEXT,
            region_id INTEGER,
            FOREIGN KEY (region_id) REFERENCES Region(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE District (
            id INTEGER PRIMARY KEY,
            name TEXT,
            forest_id INTEGER,
            FOREIGN KEY (forest_id) REFERENCES Forest(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE Station (
            id INTEGER PRIMARY KEY,
            name TEXT,
            district_id INTEGER,
            FOREIGN KEY (district_id) REFERENCES District(id)
        )
    ''')

    cursor.execute("INSERT INTO Region (id, name) VALUES (1, 'Region 1')")
    cursor.execute("INSERT INTO Forest (id, name, region_id) VALUES (1, 'Forest 1', 1)")
    cursor.execute("INSERT INTO District (id, name, forest_id) VALUES (1, 'District 1', 1)")
    cursor.execute("INSERT INTO Station (id, name, district_id) VALUES (1, 'Station 1', 1)")

    conn.commit()

    yield conn

    # Close the connection and clean up
    conn.close()


def test_get_regions(test_db):
    response = client.get('/regions')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'Region 1'}]


def test_get_forests(test_db):
    response = client.get('/forests')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'Forest 1', 'region_id': 1}]


def test_get_districts(test_db):
    response = client.get('/districts')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'District 1', 'forest_id': 1}]


def test_get_stations(test_db):
    response = client.get('/stations')
    assert response.status_code == 200
    assert response.json() == [{'id': 1, 'name': 'Station 1', 'district_id': 1}]