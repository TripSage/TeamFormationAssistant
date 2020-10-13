import time
from flask import Flask, redirect, jsonify
from flask import request
import mysql.connector as mysql
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

connection = mysql.connect(
    host="localhost",
    user="root",
    password="DatabasePass@54",
    database="teamformationassistant",
    auth_plugin='mysql_native_password'
)


@app.route('/executeAlgo')
def execute_algo():
    exec(open("algo.py").read())
    # exec(open("algo.py").read())
    return {
        'msg': 'success',
    }


@app.route('/getResults', methods=['GET'])
def get_team_data():
    cur = connection.cursor(buffered=True, dictionary=True)
    query = 'select * from Team'
    cur.execute(query)
    data = cur.fetchall()
    print(json.dumps(data))
    return json.dumps(data)


@app.route('/Signup', methods=['GET', 'POST'])
def signup():
    name = str(request.form['name'])
    hourly_rate = str(request.form['hourlyrate'])
    dob = str(request.form['dob'])
    languages = str(request.form['languages'])
    is_assigned = str(0)
    member_role = str(request.form['memberrole'])
    experience = str(request.form['experience'])
    skill_score = str(request.form['skillscore'])
    available_hours_per_week = str(request.form['availablehoursperweek'])

    if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO Member (MemberName,HourlyRate,DOB,Languages,IsAssigned,MemberRole,Experience,SkillScore,AvailableHoursPerWeek) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql, (
            name, hourly_rate, dob, languages, is_assigned, member_role, experience, skill_score,
            available_hours_per_week))
        connection.commit()
    return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success")


@app.route('/ProjectDetails', methods=['GET', 'POST'])
def projectDetails():
    name = str(request.form['name'])
    end_date = str(request.form['enddate'])
    team_size = str(request.form['teamsize'])
    budget = str(request.form['budget'])
    tools = str(request.form['tools'])
    priority = str(request.form['priority'])
    is_assignment_complete = str(0)
    if connection.is_connected():
        cursor = connection.cursor()
        sql = "INSERT INTO Project (ProjectName,ProjectEndDate,ProjectTeamSize,Budget,Tools,Priority,IsAssignmentComplete) VALUES (%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql, (name, end_date, team_size, budget, tools, priority, is_assignment_complete))
        connection.commit()
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
                cursor = connection.cursor()
                sql = "CALL populateRequirements (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, (
                    language_preferred, skill, member_role, available_hours_per_week, skill_weight, experience_weight,
                    hours_weight, language_weight, budget_weight))
                connection.commit()
                i += 1

            else:
                break

    return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success");
