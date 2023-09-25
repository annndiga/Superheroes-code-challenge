from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey


db = SQLAlchemy()

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))

    powers = db.relationship('HeroPower', back_populates='power')

    def validate_description(self, description):
        if len(description) > 255:
            raise ValueError('Description exceeds maximum length of 255 characters')

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    super_name = db.Column(db.String(255))

    hero_powers = db.relationship('HeroPower', back_populates='hero')

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(255))
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'))
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'))

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='powers')

    def validate_strength(self, strength):
        allowed_strengths = ["Strong", "Weak", "Average"]
        if strength not in allowed_strengths:
            raise ValueError('Invalid strength value. Allowed values are: Strong, Weak, Average')


