__author__ = 'aaronmsmith'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views

