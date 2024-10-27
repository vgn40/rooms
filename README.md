Rooms API
A Flask API for managing guest and booking records in a SQLite database, with endpoints for CRUD operations.

Project Structure
app.py: Main API file.
db.py: Initializes the database.
guests.db: SQLite database file.
Dockerfile: Docker setup.
requirements.txt: Python dependencies.
API Endpoints
Guests
GET /guests: Get all guests.
POST /guests: Add a new guest.
Body:
json
Kopier kode
{ "first_name": "John", "last_name": "Doe", "country": "USA" }
GET /guests/<id>: Get a guest by ID.
PUT/PATCH /guests/<id>: Update a guest.
Body:
json
Kopier kode
{ "first_name": "Jane" }
DELETE /guests/<id>: Delete a guest by ID.
Bookings
GET /bookings: Get all bookings.
POST /bookings: Add a new booking.
Body:
json
Kopier kode
{ "days_rented": 3, "season": "Summer", "price": 120.5, "date": "2023-08-01", "guest_id": 1, "room_type": "Deluxe" }
GET /bookings/<id>: Get a booking by ID.
PUT/PATCH /bookings/<id>: Update a booking.
Body:
json
Kopier kode
{ "price": 150.0 }
DELETE /bookings/<id>: Delete a booking by ID.
Setup
Initialize the Database:
bash
Kopier kode
python db.py
Install Dependencies:
bash
Kopier kode
pip install -r requirements.txt
Run the App:
bash
Kopier kode
python app.py
Docker
Build:
bash
Kopier kode
docker build -t rooms-api .
Run:
bash
Kopier kode
docker run -p 5000:5000 rooms-api
