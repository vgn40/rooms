import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/guests", methods=['GET', 'POST'])
def guests():
    conn = sqlite3.connect('guests.db')
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute('SELECT * FROM guests')
        result = cursor.fetchall()

        if not result:
            return jsonify([])

        guests = []

        for row in result:
            guest = {
                "id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "country": row[3]
            }
            guests.append(guest)

        conn.close()
        
        return jsonify(guests)
    
    elif request.method == 'POST':
        data = request.get_json()
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        country = data.get('country')

        cursor.execute('''
            INSERT INTO guests (first_name, last_name, country)
            VALUES (?, ?, ?)
        ''', (first_name, last_name, country))
        
        guest_id = cursor.lastrowid

        conn.commit()
        conn.close()

        new_guest = {
            "id": guest_id,
            "first_name": first_name,
            "last_name": last_name,
            "country": country
        }
        
        return jsonify(new_guest), 201
    

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