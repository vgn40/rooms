import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/bookings", methods=['GET', 'POST'])
def bookings():
    conn = sqlite3.connect('bookings.db')
    cursor = conn.cursor()
    
    # Get Booking
    if request.method == 'GET':
        cursor.execute('SELECT * FROM bookings')
        result = cursor.fetchall()

        if not result:
            conn.close()
            return jsonify([])

        bookings = []

        for row in result:
            booking = {
                "id": row[0],
                "days_rented": row[1],
                "season": row[2],
                "price": row[3],
                "date": row[4],
                "guest_id": row[5],
                "room_type": row[6]
            }
            bookings.append(booking)
        conn.close()
        
        return jsonify(bookings)
    
    elif request.method == 'POST':
        data = request.get_json()
        days_rented = data.get('days_rented')
        season = data.get('season')
        price = data.get('price')
        date = data.get('date')
        guest_id = data.get('guest_id')
        room_type = data.get('room_type')

        if not all([days_rented, season, price, date, guest_id, room_type]):  
            conn.close()
            return jsonify({'error': 'Missing required fields'}), 400    
        
        cursor.execute('''
            INSERT INTO bookings (days_rented, season, price, date, guest_id, room_type)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (days_rented, season, price, date, guest_id, room_type))
        booking_id = cursor.lastrowid    

        conn.commit()
        conn.close()

        new_booking = {
            "id": booking_id,
            "days_rented": days_rented,
            "season": season,
            "price": price,
            "date": date,
            "guest_id": guest_id,
            "room_type": room_type
        }
        return jsonify(new_booking), 201

@app.route("/guests/<int:id>", methods=['GET','DELETE', 'PUT', 'PATCH'])
def guest(id):
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT * FROM guests WHERE id = ?', (id,))
        result = cursor.fetchone()

        if result is None:
            return jsonify({"error": "Guest not found"}), 404

        
        guest = {
            "id": result[0],
            "first_name": result[1],
            "last_name": result[2],
            "country": result[3]
        }

        conn.close()
        
        return jsonify(guest)
    
    elif request.method == 'DELETE':
        cursor.execute('DELETE FROM guests WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Guest not found"}), 404
        
        return "", 204

    elif request.method in ['PUT', 'PATCH']:
        data = request.get_json()
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        country = data.get("country")

        cursor.execute('''
            UPDATE guests 
            SET first_name = COALESCE(?, first_name), 
                last_name = COALESCE(?, last_name), 
                country = COALESCE(?, country)
            WHERE id = ?
        ''', (first_name, last_name, country, id))

        conn.commit()

        if cursor.rowcount == 0:
            return jsonify({"error": "Guest not found"}), 404

        conn.close()
        return jsonify({"message": "Guest updated successfully"}), 200
    

if __name__ == "__main__":
    app.run(debug=True)