from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random 

engine = create_engine('sqlite:///instance/app.db')  
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Power(Base):
    __tablename__ = 'powers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

class Hero(Base):
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    super_name = Column(String, nullable=False)

class HeroPower(Base):
    __tablename__ = 'hero_powers'

    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('heroes.id'), nullable=False)
    power_id = Column(Integer, ForeignKey('powers.id'), nullable=False)
    strength = Column(String)

    

def main():
    Base.metadata.create_all(engine)

    powers = [
        Power(name="super strength", description="gives the wielder super-human strengths"),
        Power(name="flight", description="gives the wielder the ability to fly through the skies at supersonic speed"),
        Power(name="super human senses", description="allows the wielder to use her senses at a super-human level"),
        Power(name="elasticity", description="can stretch the human body to extreme lengths")
    ]

    
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra")
    ]

    print("🦸‍♀️ Seeding powers...")
    for power in powers:
        session.add(power)

    print("🦸‍♀️ Seeding heroes...")
    for hero in heroes:
        session.add(hero)

    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]

    for hero in heroes:
        session.add(hero)
        session.commit()  
        for _ in range(random.randint(1, 3)):
            power = random.choice(powers)
            strength = random.choice(strengths)
            hero_power = HeroPower(hero_id=hero.id, power_id=power.id, strength=strength)
            session.add(hero_power)


    session.commit()
    print("🦸‍♀️ Done seeding!")

if __name__ == "__main__":
    main()