#!/usr/bin/python
# coding: utf-8
import unittest
from unittest.mock import patch
import app
from blog import Blog


class AppTest(unittest.TestCase):
    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 post)')
