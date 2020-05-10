#!/usr/bin/python
# coding: utf-8
import unittest
from unittest.mock import patch
from mock import MagicMock

import app
from blog import Blog


class AppTest(unittest.TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input') as mocked_input:
            app.menu()
            mocked_input.assert_called_once_with('Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: ')

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            # The following with clause is necessary in order to stop input function waiting for user input forever
            # The patch for builtins.input fakes the execution and pretends as if the user types 'q'
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_once_with()

    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Test by Test Author (0 post)')

    """
    def test_print_blogs_with_MagicMock(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        magic_method = MagicMock('builtins.print')
        app.print_blogs()
        magic_method.assert_called_with('- Test by Test Author (0 post)')
    """
