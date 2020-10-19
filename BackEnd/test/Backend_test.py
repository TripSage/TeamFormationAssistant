import unittest
'''Define all test cases as test_TEST_NAME'''

from BackEnd.api import app
from BackEnd.connection import connect


class Api(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.db = connect()

    def test_get_team_data(self):
        '''Defining Test case for asserting get_team_data exists'''
        client = app.test_client(self)
        response = client.get('/getResults', content_type='json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()