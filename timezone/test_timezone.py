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

class TestTimezone(unittest.TestCase):

    def test_1_get_timezone(self):
        header = {'Authorization': get_authorization_token(self)}

        response = requests.get(f'{URL}/timezone', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        verify = json_data[0]
        assert_in('id', verify)
        assert_equal(type(verify['id']), int)

        assert_in('name', verify)
        assert_equal(type(verify['name']), str)

        assert_in('timeAdjustment', verify)
        assert_equal(type(verify['timeAdjustment']), str)

        assert_in('active', verify)
        assert_equal(type(verify['active']), bool)