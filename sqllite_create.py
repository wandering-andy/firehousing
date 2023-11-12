import sqlite3

# Connect to the database
conn = sqlite3.connect('fs.db')
cursor = conn.cursor()

# Create the tables
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

# Commit the changes and close the connection
conn.commit()
conn.close()
