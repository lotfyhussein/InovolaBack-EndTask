# InovolaBack-EndTask

This repo contains my implementation for Inovola Back-End Task

# Installation

- `cd ~/InovolaBack-EndTask/` after you've cloned the repo
- run `pip install -r requirements.txt` to install the dependencies
- create a file `.env` under `InovolaBack-EndTask/CoffeeScreens/` directory, and add the following to it:
  - ENVIRONMENT= `PRODUCTION` || `SANDBOX`
  - DB_NAME='YOUR_DTABASE_NAME'
  - DB_HOST='YOUR_DB_HOST' (e.g, DB_HOST='127.0.0.1' for running locally)
  - DB_PORT=YOUR_DB_PORT  (e.g, DB_PORT=27017)
- run `python manage.py migrate` to apply migrations to your database
- run `python manage.py shell < fill_db.py ` to fill the database with test data
- run `python manage.py runserver 8000` to start the server


# Running Unit Tests

- `cd ~/InovolaBack-EndTask/`
- run `python manage.py test Coffee.tests`

# API Documentation:

Coffee Machines:
| method | path | desc |
| ------------- | ------------- |------------- |
| GET | /api/coffeemachine/ | Get all coffee machines
| GET | /api/coffeemachine/?product_type=COFFEE_MACHINE_LARGE | Get only large coffee machines
| GET | /api/coffeemachine/?product_type=COFFEE_MACHINE_LARGE&water_line_compatible=True | Get large coffee machines that are water line compatible
| GET | /api/coffeemachine/?product_type=COFFEE_MACHINE_LARGE&water_line_compatible=True&model=BASE | Get large coffee machines that are water line compatible with a base model
| POST | /api/coffeemachine/ | Create a new coffee mcahine object. 
| PUT | /api/coffeemachine/{id}/ | Update a specific object. 
| DELETE | /api/coffeemachine/{id}/ | Delete a specific object. 


Coffee Pods:
| method | path | desc |
| ------------- | ------------- |------------- |
| GET | /api/coffeepod/ | Get all coffee pods
| GET | /api/coffeepod/?product_type=COFFEE_POD_LARGE | Get only large coffee pods
| GET | /api/coffeepod/?product_type=COFFEE_POD_LARGE&pack_size=3 | Get large coffee pods with pack_size = 3
| GET | /api/coffeepod/?product_type=COFFEE_POD_LARGE&pack_size=3&coffee_flavor=COFFEE_FLAVOR_CARAMEL | Get large coffee pods with pack_size = 3 and caramel flavor
| POST | /api/coffeepod/ | Create a new coffee pod object. 
| PUT | /api/coffeepod/{id}/ | Update a specific object. 
| DELETE | /api/coffeepod/{id}/ | Delete a specific object. 

# Deployed version:

  - I created a deployed version on Heroku that can be accessed directly here: [https://coffee-screens.herokuapp.com/]
  - As such, APIs can be directly accessed. (e.g,[https://coffee-screens.herokuapp.com/api/coffeepod/1/]

