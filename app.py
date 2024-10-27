import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/bookings", methods=['GET', 'POST'])
def bookings():
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()
    
    # Get all Booking
    if request.method == 'GET':
        cursor.execute('SELECT * FROM bookings')
        result = cursor.fetchall()

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
        
        # Return booking JSON message
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

@app.route("/bookings/<int:id>", methods=['GET','DELETE', 'PUT', 'PATCH'])
def booking(id):
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()


    if request.method == 'GET':
        cursor.execute('SELECT * FROM bookings WHERE id = ?', (id,))
        result = cursor.fetchone()

        if result is None:
            conn.close()
            return jsonify({"error": "Booking not found"}), 404

        
        booking = {
            "id": result[0],
            "days_rented": result[1],
            "season": result[2],
            "price": result[3],
            "date": result[4],
            "guest_id": result[5],
            "room_type": result[6]
        }

        conn.close()
        
        return jsonify(booking)
    
    elif request.method == 'DELETE':
        cursor.execute('DELETE FROM bookings WHERE id = ?', (id,))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "Booking not found"}), 404
        conn.close()
        return "", 204

    elif request.method in ['PUT', 'PATCH']:
        data = request.get_json()

        days_rented = data.get("days_rented")
        season = data.get("season")
        price = data.get("price")
        date = data.get("date")
        room_type = data.get("room_type")
        
        cursor.execute('''
            UPDATE bookings 
            SET days_rented = COALESCE(?, days_rented), 
                season = COALESCE(?, season), 
                price = COALESCE(?, price), 
                date = COALESCE(?, date), 
                room_type = COALESCE(?, room_type)
            WHERE id = ?
        ''', (days_rented, season, price, date, room_type, id))
        conn.commit()

        if cursor.rowcount == 0:
            conn.close()
            return jsonify({"error": "booking not found"}), 404

        conn.close()
        return jsonify({"message": "booking updated successfully"}), 200
    

if __name__ == "__main__":
    app.run(debug=True)