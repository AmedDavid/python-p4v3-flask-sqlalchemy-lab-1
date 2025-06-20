#!/usr/bin/env python3

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from flask import Flask, make_response
from flask_migrate import Migrate
from server.models import db, Earthquake
import traceback

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/')
def index():
    return make_response({'message': 'Flask SQLAlchemy Lab 1'}, 200)

@app.route('/earthquakes/<int:id>')
def earthquake_by_id(id):
    try:
        earthquake = Earthquake.query.filter_by(id=id).first()
        if earthquake:
            return make_response(earthquake.to_dict(), 200)
        else:
            return make_response({'message': f'Earthquake {id} not found.'}, 404)
    except Exception as e:
        print(f"Error in earthquake_by_id: {str(e)}")
        print(traceback.format_exc())
        return make_response({'error': 'Internal Server Error'}, 500)

@app.route('/earthquakes/magnitude/<float:magnitude>')
def earthquakes_by_magnitude(magnitude):
    try:
        earthquakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
        quakes_data = [quake.to_dict() for quake in earthquakes]
        return make_response({
            'count': len(quakes_data),
            'quakes': quakes_data
        }, 200)
    except Exception as e:
        print(f"Error in earthquakes_by_magnitude: {str(e)}")
        print(traceback.format_exc())
        return make_response({'error': 'Internal Server Error'}, 500)

if __name__ == '__main__':
    app.run(port=5555, debug=True)