# e-taxi Ride Sharing API


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

## Installation

1. Clone the repository:
   git clone https://github.com/ashikos/e-taxi.git

## navigate to the project directory:
cd e_taxi


## Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


## Install the project dependencies:
pip install -r requirements.txt


## Apply database migrations:
python manage.py migrate


## Create a superuser to access the Django admin:
python manage.py createsuperuser

 
# Start the development server:
python manage.py runserver



## Usage
The Vendor Management System provides APIs to manage vendors and track purchase orders. Detailed documentation for API endpoints and data models can be found in the API Endpoints section below


API Endpoints

    All the APIs except Singnup, login are secured by Jwt Authentication.
    User need to singup and login inorder to access all other Endpoints.
    A JWT token is received after the succefull login, these tokens sholud be saved in the cookies in order to 
    acccess other api Endpoints.
   
    
    Authentication:
        POST /ride/signup/ : create a new user
        POST /ride/login/ : login api which generates a jwt token which should be attached in cookies.
        GET /ride/user/ : get details of logged user
        POST /ride/logout/ : logout api 

    Create Driver Api:
        POST /ride/driver/: Create a new driver.
        GET /ride/driver/: List all drivers.
         	params = [status, is_available, serach_keyword]
        GET /ride/driver/{driver_id}/: Retrieve a specific driver's details.
        PATCH /ride/driver/{driver_id}/: Update a driver's details.
        DELETE /ride/driver/{driver_id}/: Delete a driver.

    Ride Tracking api:
        POST /ride/ride/: Create a ride request.
        GET /ride/ride/: List all get ride requests with an option to filter by status.
        GET /ride/ride/{ride_id}/: Retrieve details of a specific ride.
        PUT /ride/ride/{ride_id}/: Update a ride request.
        DELETE /ride/ride/{ride_id}/: Delete a a ride request.

    API endpoint for drivers to accept a ride request:
        patch /ride/<int:pk>/accept/ : matches driver for ride  





