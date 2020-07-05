# ChatingApp Using Flask-SocketIO

## Introduction
This is a chat application, implemented using Flask-SocketIO and it has been deployed in Heroku.


### Run app
Use the link to access my deployed version of [it](https://pulihor.herokuapp.com/) directly.

### Modify app
1. Modify application.py to replace the secret key *(i.e. os.environ.get('SECRET'))* with a secret key of your choice and the database link *(i.e. os.environ.get('DATABASE_URL'))* with the link to your own database.

2. Edit *create.py* to once again replace *os.environ.get('DATABASE_URL')* with the link to your database.

3. Run *create.py* from the terminal to create the table to hold user credentials.

