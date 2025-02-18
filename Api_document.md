
# Heart Rate Monitoring API

This API provides endpoints for managing users, patients, and heart rate records.

## Base URL
```
http://127.0.0.1:8000/api/
```

---

## Endpoints

### 1. Users

#### Get All Users
```http
GET /users/
```
**Response:**
```json
[
  {
    "id": 1,
    "email": "user@example.com"
  }
]
```

#### Create a User
```http
POST /users/
```
**Request Body:**
```json
{
  "email": "newuser@example.com",
  "password": "securepassword"
}
```

#### Get a User by ID
```http
GET /users/{id}/
```

#### Update a User
```http
PUT /users/{id}/
```
**Request Body:**
```json
{
  "email": "updated@example.com"
}
```

#### Delete a User
```http
DELETE /users/{id}/
```

---

### 2. Patients

#### Get All Patients
```http
GET /patients/
```

#### Create a Patient
```http
POST /patients/
```
**Request Body:**
```json
{
  "name": "John Doe",
  "age": 45,
  "user": 1
}
```

#### Get a Patient by ID
```http
GET /patients/{id}/
```

#### Update a Patient
```http
PUT /patients/{id}/
```

#### Delete a Patient
```http
DELETE /patients/{id}/
```

---

### 3. Heart Rate Records

#### Get All Heart Rate Records
```http
GET /heart_rate/
```

#### Create a Heart Rate Record
```http
POST /heart_rate/
```
**Request Body:**
```json
{
  "patient": 1,
  "bpm": 75,
  "recorded_at": "2025-02-17T10:00:00Z"
}
```

#### Get a Heart Rate Record by ID
```http
GET /heart_rate/{id}/
```

#### Update a Heart Rate Record
```http
PUT /heart_rate/{id}/
```

#### Delete a Heart Rate Record
```http
DELETE /heart_rate/{id}/
```

---

## Authentication
Currently, no authentication is enforced. Implement authentication if required.

## Response Codes
- `200 OK` - Successful request
- `201 Created` - Resource created successfully
- `400 Bad Request` - Invalid request data
- `404 Not Found` - Resource not found
- `500 Internal Server Error` - Server-side error

## Notes
- Ensure all required fields are included in requests.
- Use correct `id` values for updates and deletions.
- `recorded_at` should be in ISO 8601 format.

---

## Contact
For any issues, contact **admin@example.com**.

```

Let me know if you need changes or additions! 🚀