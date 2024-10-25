import sqlite3
import csv

def initialize_db():
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            country TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()
    print("Database and table 'guests' initialized successfully.")


def populate_db():
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()

    with open("international_names_with_rooms_1000.csv", mode='r', newline='', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            cursor.execute('''
                INSERT INTO guests (first_name, last_name, country)
                VALUES (?, ?, ?)
            ''', (row['First Name'], row['Family Name'], row['Country']))

    conn.commit()
    conn.close()
    print("Database populated successfully from CSV file.")


if __name__ == "__main__":
    initialize_db()
    populate_db()