# Getting Started

# installations

Download and install python `https://www.python.org/downloads/`
install following packages
    1. `djangorestframework`
    2. `Flask`
    3. `Flask-Cors`
    4. `Flask-SQLAlchemy`
    5. `SPARQLWrapper`
    6. `SQLAlchemy`
    7. `flask_restful`
    8. `django`
    9. `certifi`

# Build and Test

Go to MilitaryDefenseApp folder
Run `manage.py makemigrations` for creating migrations of database changes
Run `manage.py runmigrations` for executing database migrations to the database
Run `manage.py createsuperuser` for creating initial super admin(give username, password, and other information)

Run `manage.py runserver` for running the Django server(`http://localhost:8000/admin`)

Go to `http://localhost:8000/admin` and login with the super admin created and add users, soldiers, commanders and army camps.

Run `python main.py` for running the API server(`http://localhost:5000/`)
