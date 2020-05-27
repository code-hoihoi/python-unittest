import json

from tests.system.base_test import BaseTest


class TestHome(BaseTest):  # Notice TestCase inheritance is switched to BaseTest inheritance
    def test_home(self):
        with self.app() as c:
            response = c.get('/')
            print(response.data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(
                json.loads(response.get_data()),
                {'message': 'Hello World!'}
            )
