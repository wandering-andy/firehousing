import unittest
import sqlite3


class TestDatabaseCreation(unittest.TestCase):
    def setUp(self):
        # Connect to an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Create the tables
        self.cursor.execute('''
            CREATE TABLE Region (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE Forest (
                id INTEGER PRIMARY KEY,
                name TEXT,
                region_id INTEGER,
                FOREIGN KEY (region_id) REFERENCES Region(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE District (
                id INTEGER PRIMARY KEY,
                name TEXT,
                forest_id INTEGER,
                FOREIGN KEY (forest_id) REFERENCES Forest(id)
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE Station (
                id INTEGER PRIMARY KEY,
                name TEXT,
                district_id INTEGER,
                FOREIGN KEY (district_id) REFERENCES District(id)
            )
        ''')

    def tearDown(self):
        # Close the connection and clean up
        self.conn.close()

    def test_tables_exist(self):
        # Check if the tables exist
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = self.cursor.fetchall()

        table_names = [table[0] for table in tables]
        self.assertIn("Region", table_names)
        self.assertIn("Forest", table_names)
        self.assertIn("District", table_names)
        self.assertIn("Station", table_names)

    def test_foreign_key_constraints(self):
        # Check if the foreign key constraints are set up correctly
        self.cursor.execute("PRAGMA foreign_keys = ON")

        # Insert data with invalid foreign keys
        self.cursor.execute("INSERT INTO Forest (id, name, region_id) VALUES (1, 'Forest 1', 10)")
        self.cursor.execute("INSERT INTO District (id, name, forest_id) VALUES (1, 'District 1', 20)")
        self.cursor.execute("INSERT INTO Station (id, name, district_id) VALUES (1, 'Station 1', 30)")

        # Commit the changes and check if any errors occur due to foreign key constraints
        with self.assertRaises(sqlite3.IntegrityError):
            self.conn.commit()


if __name__ == '__main__':
    unittest.main()