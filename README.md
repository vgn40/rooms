# Guests API

This API allows you to manage guest records in a SQLite database. You can perform CRUD operations such as retrieving, adding, updating, and deleting guest information.

## Endpoints

- **GET /guests**  
  Retrieves a list of all guests.

  **Response**:  
  - `200 OK` with a JSON array of guests:
    ```json
    [
        {
            "id": 1,
            "first_name": "Liam",
            "last_name": "Nguyen",
            "country": "China"
        },
        ...
    ]
    ```
  - If no guests are found, returns an empty array: `[]`.

- **POST /guests**  
  Adds a new guest to the database.

  **Request Body**:
  ```json
  {
      "first_name": "John",
      "last_name": "Doe",
      "country": "USA"
  }

**Response**:  
- `201 Created` with the newly created guest:
  ```json
  [
      {
          "id": 1,
          "first_name": "Liam",
          "last_name": "Nguyen",
          "country": "China"
      },
      ...
  ]
  ```
-

- **GET /guests/int:id**  
  Retrieves a specific guest by ID.

  **Response**:  
  - `200 OK` with guest details:
    ```json
    [
        {
            "id": 1,
            "first_name": "Liam",
            "last_name": "Nguyen",
            "country": "China"
        },
        ...
    ]
    ```
  - `404 Not Found` if the guest does not exist.

  - **DELETE /guests/int:id**  
  Deletes a guest by ID.

  **Response**:  
  - `204 No Content` if the deletion is successful.
  - `404 Not Found` if the guest does not exist

  - **PUT OR PATCH /guests/int:id**  
  Updates the details of a guest.

  **Request Body**:
  ```json
  {
      "first_name": "John",
      "last_name": "Doe",
      "country": "USA"
  }
  
**Response**:  
- `200 OK` with a success message if updated successfully:
  ```json
  [
      {
          "message": "Guest updated successfully"
      },
      ...
  ]
  ```
- `404 Not Found` if the guest does not exist.