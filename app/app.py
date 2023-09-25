#!/usr/bin/env python3from flask import Flask, jsonify, request

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)


@app.route('/')
def home():
    return 'Welcome to the Superheroes API!'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_data = []

    for hero in heroes:
        hero_info = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name
        }
        hero_data.append(hero_info)

    return jsonify(hero_data)


@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        hero_info = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': []
        }
        for hero_power in hero.hero_powers:  
            power_info = {
                'id': hero_power.power.id,  
                'name': hero_power.power.name,
                'description': hero_power.power.description
            }
            hero_info['powers'].append(power_info)

        return jsonify(hero_info)
    else:
        return jsonify({'error': 'Hero not found'}), 404
    
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    power_data = []

    for power in powers:
        power_info = {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
        power_data.append(power_info)

    return jsonify(power_data)
    

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)

    if power:
        power_info = {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
        return jsonify(power_info)
    else:
        return jsonify({'error': 'Power not found'}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = session.query(Power).get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    new_description = request.json.get('description')
    if not new_description:
        return jsonify({"errors": ["description is required"]}), 400
    if len(new_description) < 20:
        return jsonify({"errors": ["description must be at least 20 characters long"]}), 400

    power.description = new_description
    session.commit()

    power_data = {"id": power.id, "name": power.name, "description": power.description}
    return jsonify(power_data)

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

   
    hero = session.query(Hero).get(hero_id)
    power = session.query(Power).get(power_id)

    if not hero or not power:
        return jsonify({"error": "Hero or Power not found"}), 404


if __name__ == '__main__':
    app.run(port=5555)
                                                                                                                                                                                                                                                                                                                                                                                     