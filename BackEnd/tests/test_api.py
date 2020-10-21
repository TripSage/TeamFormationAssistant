from __future__ import absolute_import

import json
import unittest
import sys

sys.path.append(".")
from app.connection import connect
from app import app

TEST_DATA = {
    "name": "XYZ",
    "hourlyrate": 40.0,
    "dob": "Sat, 03 Oct 1998 00:00:00 GMT",
    "languages": "JAVA",
    "memberrole": "Frontend Software Engineer",
    "experience": 2,
    "skillscore": 70,
    "availablehoursperweek": 40
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

    def test_member_signup(self):
        response = self.app.post('http://localhost:5000/Signup/', data=json.dumps(TEST_DATA, indent=4))
        print(response.get_data())
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
