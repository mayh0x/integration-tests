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

class TestPermissions(unittest.TestCase):

    def test_1_get_permissions(self):
        header = {'Authorization': get_authorization_token(self)}

        response = requests.get(f'{URL}/permissions', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        verify = json_data[0]
        assert_in('id', verify)
        assert_equal(type(verify['id']), int)

        assert_in('name', verify)
        assert_equal(type(verify['name']), str)

        assert_in('adviser', verify)
        assert_equal(type(verify['adviser']), bool)

        assert_in('achiever', verify)
        assert_equal(type(verify['achiever']), bool)

        assert_in('administrator', verify)
        assert_equal(type(verify['administrator']), bool)

        assert_in('coordinator', verify)
        assert_equal(type(verify['coordinator']), bool)

        assert_in('active', verify)
        assert_equal(type(verify['active']), bool)

        assert_in('tag', verify)
        assert_equal(type(verify['tag']), str)