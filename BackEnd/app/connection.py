# pylint: skip-file
import mysql.connector as conn

# Connect to Local MYSQL database on Dev team Desktops. FOr production Environments connect to AWS
try:
    Connection = conn.connect(
        host="localhost",
        user="root",
        password="DatabasePass@54",
        database="teamformationassistant",
        auth_plugin="mysql_native_password",
    )
    print("Connected to Developer Database")
except:
    Connection = conn.connect(
        host="sefall2021.cosnmrdyk6wi.us-east-2.rds.amazonaws.com",
        user="root",
        password="SEFall2021",
        database="teamformationassistant",
    )
    print("Switching to AWS DataBase")


def connect():
    try:
        Connection = conn.connect(
            host="localhost",
            user="root",
            password="DatabasePass@54",
            database="teamformationassistant",
            auth_plugin="mysql_native_password",
        )
    except:
        Connection = conn.connect(
            host="sefall2021.cosnmrdyk6wi.us-east-2.rds.amazonaws.com",
            user="root",
            password="SEFall2021",
            database="teamformationassistant",
        )


def CheckConnection():
    if not Connection.is_connected():
        connect()


def get_all_team_data():
    """Returns Team Assignment data for members who have already been assigned to a team"""
    # ToDo: Create Modified Query to show further data of each member by joining with member table
    # ToDo: To overcome Privacy Concerns, show only the data of team members
    CheckConnection()
    with Connection.cursor(buffered=True, dictionary=True) as cursor:
        cursor.execute("select * from Team;")
        data = cursor.fetchall()
    return data


def get_all_member_data():
    """Returns Member details present in the DB"""
    # ToDo: Create Modified Query to show further data of each member by joining with member table
    # ToDo: To overcome Privacy Concerns, show only the data of team members
    CheckConnection()
    with Connection.cursor(buffered=True, dictionary=True) as cursor:
        cursor.execute("select * from Member;")
        data = cursor.fetchall()
    return data


def add_member(data):
    """Adds the newly signed up user to the member Table"""
    # ToDo: Get Project Details from user during signup. Current system assumes user has no project preference.

    try:
        CheckConnection()
        with Connection.cursor() as cursor:
            name = str(data["name"])
            hourly_rate = str(data["hourlyrate"])
            dob = str(data["dob"])
            languages = str(data["languages"])
            is_assigned = str(0)
            member_role = str(data["memberrole"])
            experience = str(data["experience"])
            skill_score = str(data["skillscore"])
            available_hours_per_week = str(data["availablehoursperweek"])

            query = "INSERT INTO Member (MemberName,HourlyRate,DOB,Languages,IsAssigned,MemberRole,Experience,SkillScore,AvailableHoursPerWeek) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(
                query,
                (
                    name,
                    hourly_rate,
                    dob,
                    languages,
                    is_assigned,
                    member_role,
                    experience,
                    skill_score,
                    available_hours_per_week,
                ),
            )
            Connection.commit()
            return True

    except conn.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        Connection.rollback()
        return False


def create_project(data):
    """Adds new project details to project database"""
    try:
        CheckConnection()
        with Connection.cursor() as cursor:
            name = str(data["name"])
            end_date = str(data["enddate"])
            team_size = str(data["teamsize"])
            budget = str(data["budget"])
            tools = str(data["tools"])
            priority = str(data["priority"])
            is_assignment_complete = str(0)

            query = "INSERT INTO Project (ProjectName,ProjectEndDate,ProjectTeamSize,Budget,Tools,Priority,IsAssignmentComplete) VALUES (%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(
                query,
                (
                    name,
                    end_date,
                    team_size,
                    budget,
                    tools,
                    priority,
                    is_assignment_complete,
                ),
            )
            Connection.commit()
        return True

    except conn.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        Connection.rollback()
        return False


def save_project_requirements(data):
    try:
        CheckConnection()
        with Connection.cursor() as cursor:
            i = 0
            for key in data.items():
                colname = "languagepreferred" + str(i)
                if colname in data:
                    language_preferred = str(data[colname])
                    skill = str(data["skill" + str(i)])
                    member_role = str(data["memberrole" + str(i)])
                    available_hours_per_week = int(
                        data["availablehoursperweek" + str(i)]
                    )
                    skill_weight = int(data["skillweight"])
                    experience_weight = int(data["experienceweight"])
                    hours_weight = int(data["hoursweight"])
                    language_weight = int(data["languageweight"])
                    budget_weight = int(data["budgetweight"])

                    sql = "CALL populateRequirements (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                    cursor.execute(
                        sql,
                        (
                            language_preferred,
                            skill,
                            member_role,
                            available_hours_per_week,
                            skill_weight,
                            experience_weight,
                            hours_weight,
                            language_weight,
                            budget_weight,
                        ),
                    )
                    Connection.commit()
                    i += 1
                else:
                    break
        return True

    except conn.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        Connection.rollback()
        return False
