import json
import os
import requests
from nose.tools import *
import sys
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
path_dir = os.path.join(ROOT_DIR, "utils")
sys.path.append(path_dir)

from main_functions import *

class TestProfiles(unittest.TestCase):

    def test_1_get_profiles(self):
        header = {'Authorization': get_authorization_token(self)}

        response = requests.get(f'{URL}/profiles', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        admin = json_data[0]
        assert_in('id', admin)
        assert_equal(type(admin['id']), int)
        assert_equal(admin['id'], 1)

        assert_in('name', admin)
        assert_equal(type(admin['name']), str)
        assert_equal(admin['name'], 'Administrator')

        assert_in('type', admin)
        assert_equal(type(admin['type']), str)
        assert_equal(admin['type'], 'ADMINISTRATOR')

        achiever = json_data[1]
        assert_in('id', achiever)
        assert_equal(type(achiever['id']), int)
        assert_equal(achiever['id'], 2)

        assert_in('name', achiever)
        assert_equal(type(achiever['name']), str)
        assert_equal(achiever['name'], 'Achiever')

        assert_in('type', achiever)
        assert_equal(type(achiever['type']), str)
        assert_equal(achiever['type'], 'ACHIEVER')

        adviser = json_data[2]
        assert_in('id', adviser)
        assert_equal(type(adviser['id']), int)
        assert_equal(adviser['id'], 3)

        assert_in('name', adviser)
        assert_equal(type(adviser['name']), str)
        assert_equal(adviser['name'], 'Adviser')

        assert_in('type', adviser)
        assert_equal(type(adviser['type']), str)
        assert_equal(adviser['type'], 'ADVISER')

        coord = json_data[3]
        assert_in('id', coord)
        assert_equal(type(coord['id']), int)
        assert_equal(coord['id'], 4)

        assert_in('name', coord)
        assert_equal(type(coord['name']), str)
        assert_equal(coord['name'], 'Coordinator')

        assert_in('type', coord)
        assert_equal(type(coord['type']), str)
        assert_equal(coord['type'], 'COORDINATOR')
