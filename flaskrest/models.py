from sqlalchemy import Column, Integer, String

from flaskrest.database import db
from flaskrest.database import Base
from flask import url_for

class User(Base):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  name = Column(String(50), unique=True)
  email = Column(String(120), unique=True)
  machines = db.relationship('Mach',backref='user',lazy='dynamic')
  def __init__(self, name=None, email=None):
    self.name = name
    self.email = email

  def __repr__(self):
    return '<User %r>' % (self.name)

class Mach(Base):
  __tablename__='mach'
  id = Column(Integer, primary_key=True)
  name = Column(String(50), unique=True)
  disk_size = Column(Integer, unique=False)
  num_nodes = Column(Integer, unique=False)
  user_id = Column(Integer,db.ForeignKey('user.id'))

  def to_json(self):
  	return{
  		'name': self.name,
  		'disk_size' : self.disk_size,
  		'num_nodes' : self.num_nodes
	}
	
  def from_json(self, json):
  	print json['name']
    	try:
    		self.name = json['name']
    	except KeyError as e:
      		raise ValidationError('Invalid..')
    	return self

  def get_url(self):
  	return url_for('new_mach', id = self.id, _external=True) 	