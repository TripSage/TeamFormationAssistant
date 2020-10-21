from __future__ import absolute_import
import unittest
import sys
sys.path.append(".")
from app.connection import connect
from app import app

'''Define all test cases as test_TEST_NAME'''

class Api(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = connect()
    
    def test_get_team_data(self):
        response = self.app.get('/getResults')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()