from unittest import TestCase

from tests.app import app


class BaseTest(TestCase):
    def setUp(self):
        # This code tells Flask that we are running a test
        app.testing = True
        self.app = app.test_client
