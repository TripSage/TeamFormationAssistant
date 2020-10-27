# ToDo: Remove CORS Dependency
# ToDo: Restructure ProjectDetails Function: High Complexity
from __future__ import absolute_import
from flask import redirect
from flask import request, jsonify
from flask_cors import CORS

from app import connection
from app import app

# app = Flask(__name__)
cors = CORS(app)

@app.route('/executeAlgo')
def execute_algo():
    exec(open("TeamAssigner.py").read())
    return {
        'msg': 'success',
    }

@app.route('/getResults', methods=['GET'])
def get_team_data():
    data = connection.get_all_team_data()
    return jsonify(data)

@app.route('/getMembers', methods=['GET'])
def get_member_data():
    data = connection.get_all_member_data()
    return jsonify(data)

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    data = request.form
    if connection.add_member(data) == True:
        return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success")


@app.route('/ProjectDetails', methods=['GET', 'POST'])
def projectDetails():
    data = data
    result = save_project_details(data)
    if result == True:
        return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success");

def save_project_details(data):
    connection.create_project(data)
    result = connection.save_project_requirements(data)
    return result
