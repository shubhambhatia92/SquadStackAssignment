import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/person', methods=['POST'])
def json_example():
    request_data = request.get_json()
    first_name = None
    last_name = None
    email = None
    org_name = None
    company_id = None
    siq_stop=None
    flag=None

    if request_data:
        if 'current' in request_data:
            if 'first_name' in request_data['current']:
                first_name = request_data['current']['first_name']

        if 'current' in request_data:
            if 'last_name' in request_data['current']:
                last_name = request_data['current']['last_name']

        if 'current' in request_data:
            if 'email' in request_data['current']:
                email = request_data['current']['email']

        if 'current' in request_data:
            if 'org_name' in request_data['current']:
                org_name = request_data['current']['org_name']

        if 'current' in request_data:
            if 'company_id' in request_data['current']:
                company_id = request_data['current']['company_id']

        if 'siq_stop' in request_data:
            siq_stop = request_data['siq_stop']

        if 'event' in request_data:
            if request_data['event']=='updated.person':
                flag='person was updated'        
            else:
                flag='person was created'    

    return '''
           The  first name is: {}
           The last name is: {}
           The email  is: {}
           The org name: {}
           The company_id is: {}
           The person was:{}
           The siq stop value:{}'''.format(first_name,last_name, email, org_name, company_id,flag,siq_stop)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


app.run()    