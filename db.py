import sqlite3
import csv

def initialize_db():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    
    cursor.execute('DROP TABLE IF EXISTS guests')

     # Create the bookings table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            days_rented INTEGER NOT NULL,
            season TEXT NOT NULL,
            price REAL NOT NULL,
            date TEXT NOT NULL,
            guest_id INTEGER NOT NULL,
            room_type TEXT NOT NULL,
            FOREIGN KEY (guest_id) REFERENCES guests(id)
        )
    ''')
    conn.commit()
    conn.close()
    print("Database and table 'booking' initialized successfully.")


#def populate_db():
#    conn = sqlite3.connect('bookings.db')
#    cursor = conn.cursor()

#   with open("international_names_with_rooms_1000.csv", mode='r', newline='', encoding='utf-8') as file:
#        csv_reader = csv.DictReader(file, delimiter=',')
#        for row in csv_reader:
#            cursor.execute('''
#    INSERT INTO bookings (days_rented, season, price, date, guest_id, room_type)
#    VALUES (?, ?, ?, ?, ?, ?)
#''', (row['days_rented'], row['season'], row['price'], row['date'], row['guest_id'], row['room_type']))
#    conn.commit()
#    conn.close()
#    print("Database populated successfully from CSV file.")


if __name__ == "__main__":
    initialize_db()
 