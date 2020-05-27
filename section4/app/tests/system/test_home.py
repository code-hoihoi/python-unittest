from unittest import TestCase
from tests.app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            response = c.get('/')
            print(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World!'}
            )
