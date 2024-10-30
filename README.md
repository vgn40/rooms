# Rooms API
A Flask API for managing booking records in a SQLite database, with endpoints for CRUD operations.

## Project Structure
* `app.py`: Main API file.
* `db.py`: Initializes the database.
* `guests.db`: SQLite database file.
* `Dockerfile`: Docker setup.
* `requirements.txt`: Python dependencies.

## API Endpoints
### Bookings
* **GET /bookings**: Get all bookings.
* **POST /bookings**: Add a new booking.
  * **Body**:
    ```json
    { "days_rented": 3, "season": "Summer", "price": 120.5, "date": "2023-08-01", "guest_id": 1, "room_type": "Deluxe" }
    ```
* **GET /bookings/<id>**: Get a booking by ID.
* **PUT/PATCH /bookings/<id>**: Update a booking.
  * **Body**:
    ```json
    { "price": 150.0 }
    ```
* **DELETE /bookings/<id>**: Delete a booking by ID.

## Setup

1. **Initialize the Database**:
   ```bash
   python db.py
