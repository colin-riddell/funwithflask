from flask import  jsonify, abort, request
from flaskrest import app

from flaskrest.database import db
from flaskrest.models import User, Mach

from sqlalchemy import exc

def unimplemented(thing={'message': 'unimplemented' }):
  response = jsonify(thing)
  response.status_code = 501
  return response


@app.route('/api/v0.1/mach/<int:_id>', methods=['GET'])
def get_mach(_id):
    m = Mach.query.get_or_404(_id)
    return jsonify(m.to_json())
  
@app.route('/api/v0.1/mach/', methods=['GET'])
def get_machs():
  thing = jsonify({'urls':[m.get_url() for m in Mach.query.all()]})
  print str(thing)
  return thing

'''
http://127.0.0.1:5000/api/v0.1/mach/

{
  'name': 'test_name',
  'disk_size' : 64,
  'num_nodes' : 6
}
'''
@app.route('/api/v0.1/mach/', methods=['POST'])
def new_mach():
  print request.json
  m = Mach().from_json(request.json)
  db.session.add(m)
  db.session.commit()
  return unimplemented()