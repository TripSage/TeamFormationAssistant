from __future__ import absolute_import

import json
import unittest
import sys

sys.path.append(".")
from app.connection import connect
from app import connection
from app import app
from flask import request, url_for

TEST_DATA = {
    "name": "XYZ",
    "hourlyrate": "40",
    "dob": "1995-10-21",
    "languages": "JAVA",
    "memberrole": "DevOps Engineer",
    "experience": "2",
    "skillscore": "70",
    "availablehoursperweek": "40"
}

WRONG_DATA = {
    "name": "XYZ",
    "hourlyrate": "40",
    "dob": "1995-100-21",
    "languages": "JAVA",
    "memberrole": "DevOps Engineer",
    "experience": "2",
    "skillscore": "70",
    "availablehoursperweek": "40"
}

PROJECT_DETAIL_DATA={
    "name": "test",
    "enddate": "2020-12-12",
    "teamsize": "1",
    "budget" :"100",
    "tools": "Vscode",
    "priority": "4",
    "languagepreferred0": "JAVA",
    "skill0": "33",
    "memberrole0": "DevOps",
    "availablehoursperweek0": "20",
    "skillweight": "20",
    "experienceweight": "20",
    "hoursweight": "20",
    "languageweight": "20",
    "budgetweight": "20"
    
}

'''Define all test cases as test_TEST_NAME'''

class Api(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = connect()
        self.connection = connection

    def test_get_team_data(self):
        response = self.app.get('/getResults')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(len(data[0]['MemberName']), 0)
        # self.assertIsNotNone(data[0]['ProjectId'])
        # self.assertNotEqual(len(data[0]['ProjectName']), 0)

    def test_member_signup_success(self):
        response = self.connection.add_member(TEST_DATA)
        self.assertEqual(response, True)

    def test_member_signup_fails(self):
        response = self.connection.add_member(WRONG_DATA)
        self.assertEqual(response, False)
    
    def test_save_project_requirements(self):
        response = self.connection.save_project_requirements(PROJECT_DETAIL_DATA)
        self.assertEqual(response, True)
    
    def create_project(self):
        response = self.connection.create_project(PROJECT_DETAIL_DATA)
        self.assertEqual(response, True)



if __name__ == '__main__':
    unittest.main()
