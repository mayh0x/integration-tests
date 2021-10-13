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

class TestLanguages(unittest.TestCase):

    def test_1_get_languages(self):
        header = {'Authorization': get_authorization_token(self)}

        response = requests.get(f'{URL}/languages', headers=header)
        assert_equal(response.status_code, 200)

        json_data = json.loads(response.content)

        pt_language = json_data[0]
        assert_in('id', pt_language)
        assert_equal(type(pt_language['id']), int)
        assert_equal(pt_language['id'], 1)

        assert_in('name', pt_language)
        assert_equal(type(pt_language['name']), str)
        assert_equal(pt_language['name'], 'Português')

        assert_in('code', pt_language)
        assert_equal(type(pt_language['code']), str)
        assert_equal(pt_language['code'], 'pt')

        en_language = json_data[1]
        assert_in('id', en_language)
        assert_equal(type(en_language['id']), int)
        assert_equal(en_language['id'], 2)

        assert_in('name', en_language)
        assert_equal(type(en_language['name']), str)
        assert_equal(en_language['name'], 'English')

        assert_in('code', en_language)
        assert_equal(type(en_language['code']), str)
        assert_equal(en_language['code'], 'en')

        # es_language = json_data[2]
        # assert_in('id', es_language)
        # assert_equal(type(es_language['id']), int)
        # assert_equal(es_language['id'], 3)
        #
        # assert_in('name', es_language)
        # assert_equal(type(es_language['name']), str)
        # assert_equal(es_language['name'], 'Español')
        #
        # assert_in('code', es_language)
        # assert_equal(type(es_language['code']), str)
        # assert_equal(es_language['code'], 'es')

        first_element = json_data[0]
        assert_in('id', first_element)
        assert_equal(type(first_element['id']), int)

        assert_in('name', first_element)
        assert_equal(type(first_element['name']), str)
