#!/usr/bin/env python3from flask import Flask, jsonify, request

from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower
 

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
    power = Power.query.get(id)

    if not power:
        return jsonify({'error': 'Power not found'}), 404

    data = request.get_json()

    if 'description' in data:
        power.description = data['description']

    try:
        db.session.commit()
        return jsonify({
            'id': power.id,
            'name': power.name,
            'description': power.description
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['Validation errors']}), 400

@app.route('/hero_powers', methods=['GET'])
def get_hero_powers():
    hero_powers = HeroPower.query.all()
    hero_power_data = []

    for hero_power in hero_powers:
        data = {
            'hero_id': hero_power.hero_id,
            'power_id': hero_power.power_id,
            'strength': hero_power.strength
        }
        hero_power_data.append(data)

    return jsonify(hero_power_data)

@app.route('/hero_powers/<int:id>', methods=['GET'])
def get_hero_power_by_id(id):
    hero_power = HeroPower.query.get(id)

    if not hero_power:
        return jsonify({'error': 'HeroPower not found'}), 404

    # Assuming HeroPower has attributes 'hero_id', 'power_id', and 'strength'
    hero_power_data = {
        'hero_id': hero_power.hero_id,
        'power_id': hero_power.power_id,
        'strength': hero_power.strength
    }

    return jsonify(hero_power_data)      

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json

    
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    power = Power.query.get(power_id)
    hero = Hero.query.get(hero_id)

    if not power or not hero:
        return jsonify({"error": "Power or Hero not found"}), 404

    hero_power = HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(hero_power)

    try:
        db.session.commit()

        hero_data = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [
                {
                    'id': power.id,
                    'name': power.name,
                    'description': power.description
                }
            ]
        }

        return jsonify(hero_data), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': ['Validation errors']}), 400
    
if __name__ == '__main__':
    app.run(port=5555)
                                                                                                                                                                                                                                                                                                                                                                                     