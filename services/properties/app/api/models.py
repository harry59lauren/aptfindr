import common
from services.properties.app import db
from sqlalchemy.sql import func

'''Class to represent an USPS postal address of property management office, apartment building, etc..'''
class Address(db.Model):


    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bldg_no = db.Column(db.String(128), nullable=False)
    street = db.Column(db.String(128), nullable=False)
    state = db.Column(db.String(2), nullable=False)
    zipcode = db.Column(db.String(11), nullable=False)


    def __init__(self, building_no:str, street:str, city:str, state:str, zipcode:(int, int)):
        self.building_no = building_no
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode




'''Class to represent a property management company'''
class PropertyManagement(db.Model):

    __tablename__ = 'property_management'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    created_date = db.Column(db.DateTime, default=func.now(), nullable=False)
    properties = db.relationship('Property', backref='property_management', lazy=True)



''' A  class to represent a single property'''
class Property(db.Model):

    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_manager_id = db.Column(db.Integer, db.ForeignKey('property_management.id'), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    buildings = db.relationship('Building', backref='property', lazy=True)


    def __init__(self, id:str, manager_id:str, name:str, address: common.Address, type:str):
        self.id = id
        self.manager_id = manager_id
        self.name = name
        self.address = address
        self.type = type


class Building(db.Model):

    __tablename__ = 'building'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    property_id = db.Column(db.Integer, db.ForeignKey('property.id'), nullable=False)
    name =  db.Column(db.String(128), nullable=False)
    units = db.relationship('Unit', backref='building', lazy=True)



class Unit(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    building_id = db.Column(db.Integer, db.ForeignKey('building.id'), nullable=False)
    unit_no = db.Column(db.Integer, nullable=False)


