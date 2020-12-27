# FLASK vs FASTAPI | ORM with SQLAlchemy
[Work in progress...]


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Flask](#flask)
* [Project Structure](#project-structure)
* [Inspiration](#inspiration)


## Technologies
Project is created with:
* FLASK
  * Flask-SQLAalchemy: Database ORM
  * Flask-Migrate: Database updates
  * Flask_Bcrypt: Encrypt passwords
  * Flask-Marshmallow: Helps with serializing and deserializing objects. Transform our SQLAlchemy objects into readable JSON data

## Setup
To run this project, install it locally using npm:

```
cd ../<project-name>
virtualenv env --python=python3.9 # Recomended
source env/bin/activate # Recomended
pip install -r requirements.txt
python run.py
```

## Flask

### Project Structure

### DATABASE SET UP - Flask-migrations

#### Flask_migrate
Flask extension that is used to migrate sqlalchemy based database models. When adding columns, migrate will compare the current version and the new version and create a script to migrate from one to the other.
Once you have data it becames very usefull extension.

##### Commands
```
python migrate.py db init # First time to create unexisting tables
```
```
python migrate.py db migrate
```
```
python migrate.py db upgrade
```


### Flask "Application Factory" Pattern

benefits:
* 1. Stop/avoid circular import;
* 2. Better and easier setup, for example, test, different environments;
* 3. More organized and readable project.


### Functional Based Structure

There are many ways to setup your project folder structure. One is by its function. For instance:
```
project/
  __init__.py
  models/
    __init__.py
    base.py
    users.py
    posts.py
    ...
  routes/
    __init__.py
    home.py
    account.py
    dashboard.py
    ...
  templates/
    base.html
    post.html
    ...
  services/
    __init__.py
    google.py
    mail.py
    ...

```

All things are grouped by its function. If it hehaves as a model, put it in models folder; if it behaves as a route, put it in routes folder. Build a create_app factory in project/__init__.py, and init_app of everything:


### Before running the server set up db if tables are not yet created

* Enter python Interpretor
```
python
```

```python
from app import db
db.create_all()
```
