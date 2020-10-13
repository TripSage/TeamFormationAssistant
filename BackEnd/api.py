# ToDo: Remove CORS Dependency
# ToDo: Restructure ProjectDetails Function: High Complexity

from flask import Flask, redirect
from flask import request, jsonify
from flask_cors import CORS

import BackEnd.connection as connection

app = Flask(__name__)
cors = CORS(app)

@app.route('/executeAlgo')
def execute_algo():
    exec(open("algo.py").read())
    return {
        'msg': 'success',
    }

@app.route('/getResults', methods=['GET'])
def get_team_data():
    data = connection.get_all_team_data()
    return jsonify(data)

@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    data = request.form
    connection.add_member(data)
    return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success")


@app.route('/ProjectDetails', methods=['GET', 'POST'])
def projectDetails():
    data = request.form
    connection.create_project(data)
    if connection.Connection.is_connected():
        i = 0

        for key in request.form.items():
            colname = 'languagepreferred' + str(i)
            if colname in request.form:
                language_preferred = str(request.form[colname])
                skill = str(request.form['skill' + str(i)])
                member_role = str(request.form['memberrole' + str(i)])
                available_hours_per_week = int(request.form['availablehoursperweek' + str(i)])
                skill_weight = int(request.form['skillweight'])
                experience_weight = int(request.form['experienceweight'])
                hours_weight = int(request.form['hoursweight'])
                language_weight = int(request.form['languageweight'])
                budget_weight = int(request.form['budgetweight'])
                cursor = connection.Connection.cursor()
                sql = "CALL populateRequirements (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (
                    language_preferred, skill, member_role, available_hours_per_week, skill_weight, experience_weight,
                    hours_weight, language_weight, budget_weight))
                connection.Connection.commit()
                i += 1

            else:
                break

    return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success");
