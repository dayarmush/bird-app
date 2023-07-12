import os

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import db, Bird

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)

@app.get('/')
def index():
    return '<h1>Hello World</h1>'

@app.get('/birds')
def get_birds():
    birds = [bird.to_dict() for bird in Bird.query.all()]
    return birds, 200