#!/usr/bin/python
# coding: utf-8
import unittest
from unittest.mock import patch
from mock import MagicMock

import app
from blog import Blog
from post import Post


class AppTest(unittest.TestCase):
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            app.menu()
            mocked_input.assert_called_once_with(app.MENU_PROMPT)

    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            # The following "with clause" is necessary in order to stop input function waiting for user input forever
            # The patch for builtins.input fakes the execution and pretends as if the user types 'q'
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called_once_with()

    def test_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with(f"- {b}\n")

    """
    def test_print_blogs_with_MagicMock(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        magic_method = MagicMock('builtins.print')
        app.print_blogs()
        magic_method.assert_called_with('- Test by Test Author (0 post)')
    """

    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Test'))

    def test_ask_read_blog(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}
        with patch('builtins.input', return_value='Test') as mocked_input:
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)

    def test_print_posts(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Post Content')
        app.blogs = {'Test': b}
        with patch('app.print_one_post') as mocked_print_post:
            app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])

    def test_print_one_post(self):
        p = Post('Test Post Title', 'Test Post Content')

        with patch('builtins.print') as mocked_print:
            app.print_one_post(p)
            mocked_print.assert_called_with(f"--- Test Post Title --- \n\n Test Post Content \n\n")
