import time
from flask import Flask, redirect
from flask import request
import mysql.connector


app = Flask(__name__)

connection = mysql.connector.connect(
    host= "localhost", 
    user= "root", 
    password= "", 
    database= "" 
)

@app.route('/executeAlgo')
def execute_algo():
    exec(open("algo.py").read())
    #exec(open("algo.py").read())
    return {
        'msg': 'success',
    }
@app.route('/Signup', methods=['GET', 'POST'])
def singup():
    name = str(request.form['name'])
    hourly_rate = str(request.form['hourlyrate'])
    dob = str(request.form['dob'])
    languages = str(request.form['languages'])
    is_assigned = str(0)
    member_role = str(request.form['memberrole'])
    experience = str(request.form['experience'])
    skill_score = str(request.form['skillscore'])
    available_hours_per_week = str(request.form['availablehoursperweek'])
    
    records = [name,hourly_rate,dob,languages,is_assigned,member_role,experience,skill_score,available_hours_per_week]
    if connection.is_connected():
        cursor = connection.cursor()
        sql =  "INSERT INTO Member (MemberName,HourlyRate,DOB,Languages,IsAssigned,MemberRole,Experience,SkillScore,AvailableHoursPerWeek) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
        cursor.execute(sql,(name,hourly_rate,dob,languages,is_assigned,member_role,experience,skill_score,available_hours_per_week))
        connection.commit()
    return redirect("http://localhost:3000/TeamFormationAssistant/Signup/Success")
