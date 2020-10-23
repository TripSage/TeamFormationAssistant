from __future__ import absolute_import

import json
import unittest
import sys

sys.path.append(".")
from app.connection import connect
from app import app

TEST_DATA = {
    "name": "XYZ",
    "hourlyrate": "40",
    "dob": "1995-10-21",
    "languages": "JAVA",
    "memberrole": "Frontend Software Engineer",
    "experience": "2",
    "skillscore": "70",
    "availablehoursperweek": "40"
}

WRONG_DATA = {
    "name": "XYZ",
    "hourlyrate": "40",
    "dob": "1995-100-21",
    "languages": "JAVA",
    "memberrole": "Frontend Software Engineer",
    "experience": "2",
    "skillscore": "70",
    "availablehoursperweek": "40"
}

'''Define all test cases as test_TEST_NAME'''


class Api(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = connect()

    def test_get_team_data(self):
        response = self.app.get('/getResults')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(len(data[0]['MemberName']), 0)
        self.assertIsNotNone(data[0]['ProjectId'])
        self.assertNotEqual(len(data[0]['ProjectName']), 0)

    def test_member_signup_success(self):
        response = self.app.post('/Signup', data=TEST_DATA)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, True)

    def test_member_signup_fails(self):
        response = self.app.post('/Signup', data=WRONG_DATA)
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, False)

if __name__ == '__main__':
    unittest.main()
