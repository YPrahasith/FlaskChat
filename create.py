from flask import Flask
import os
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://xletpeppbqjdes:623134863aad13710d791e4fdb90e0a3e220786d5c7a53dcc818fafb7d323d0c@ec2-46-137-84-140.eu-west-1.compute.amazonaws.com:5432/dfphimldchqdbj'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
