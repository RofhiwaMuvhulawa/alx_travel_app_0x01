ALX Travel App
A Django-based travel listing platform with RESTful APIs for managing listings and bookings.
Project Setup

Clone the Repository:
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app


Set Up Virtual Environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies:
pip install -r requirements.txt


Configure Environment Variables:Create a .env file in the project root with the following:
DB_NAME=alx_travel_db
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
SECRET_KEY=your_django_secret_key


Set Up MySQL Database:
mysql -u root -p
CREATE DATABASE alx_travel_db;


Run Migrations:
python manage.py makemigrations
python manage.py migrate


Seed the Database:
python manage.py seed


Run the Server:
python manage.py runserver



API Endpoints
The API is accessible at http://127.0.0.1:8000/api/. Use tools like Postman to test the endpoints.
Listings

GET /api/listings/: Retrieve all listings.
GET /api/listings/<id>/: Retrieve a specific listing.
POST /api/listings/: Create a new listing.
PUT /api/listings/<id>/: Update a listing.
DELETE /api/listings/<id>/: Delete a listing.

Bookings

GET /api/bookings/: Retrieve all bookings.
GET /api/bookings/<id>/: Retrieve a specific booking.
POST /api/bookings/: Create a new booking.
PUT /api/bookings/<id>/: Update a booking.
DELETE /api/bookings/<id>/: Delete a booking.

Testing Endpoints
Use Postman to test the API endpoints:

GET All Listings:

URL: http://127.0.0.1:8000/api/listings/
Method: GET
Expected Response: JSON list of listings (seeded data).


POST a New Listing:

URL: http://127.0.0.1:8000/api/listings/
Method: POST
Body (JSON):{
    "title": "Test Villa",
    "description": "A test villa for API testing",
    "location": "Test City",
    "price_per_night": 120.00,
    "owner": 1,
    "is_available": true
}


Expected Response: 201 Created with the new listing data.


GET a Specific Listing:

URL: http://127.0.0.1:8000/api/listings/1/
Method: GET
Expected Response: JSON of the listing with ID 1.


PUT Update a Listing:

URL: http://127.0.0.1:8000/api/listings/1/
Method: PUT
Body (JSON):{
    "title": "Updated Villa",
    "description": "Updated description",
    "location": "Test City",
    "price_per_night": 150.00,
    "owner": 1,
    "is_available": false
}


Expected Response: 200 OK with updated listing data.


DELETE a Listing:

URL: http://127.0.0.1:8000/api/listings/1/
Method: DELETE
Expected Response: 204 No Content.


Bookings Endpoints:

Similar steps apply for /api/bookings/ and /api/bookings/<id>/.
Example POST body:{
    "listing": 1,
    "user": 1,
    "start_date": "2025-08-10",
    "end_date": "2025-08-15",
    "total_price": 600.00,
    "status": "PENDING"
}





Swagger Documentation
Access API documentation at:

Swagger UI: http://127.0.0.1:8000/swagger/
ReDoc: http://127.0.0.1:8000/redoc/

Notes

Ensure MySQL is running and credentials in .env are correct.
Create a superuser for admin access: python manage.py createsuperuser.
Logs are written to request_logs.log for each request.
Restrict CORS_ALLOW_ALL_ORIGINS and ALLOWED_HOSTS in production.

