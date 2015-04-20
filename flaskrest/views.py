from flask import  jsonify, abort, request
from flaskrest import app

from flaskrest.database import db
from flaskrest.models import User

from sqlalchemy import exc

tasks = [
    {
        'id': 1,
        'title': u'do something',
        'description': u' some stuff', 
        'done': False
    },
    {
        'id': 2,
        'title': u'do somethng else',
        'description': u'Some more stuff', 
        'done': False
    }
]


@app.route('/awesome')
def awesome():
  u = User('admin', 'admin@localhost')
  try:
    db.session.add(u)
    db.session.commit()
  except exc.IntegrityError as ex:
    print ex.__class__
    return  jsonify('{\'message \': \'data not added - it was already added\'')
  return  jsonify('{\'message \': \'data  added\'')



@app.route('/api/v0.1/mach/<int:_id>', methods=['GET'])
def get_task(_id):
  task = [task for task in tasks if task['id'] == _id]
  if len(task) == 0:
    abort(404)
  return jsonify({'task': task[0]})


@app.route('/api/v0.1/mach/', methods=['POST'])
def new_task():
  print str(request.data)
  #cTODO reate a new mach
  return jsonify({'message': 'success' })