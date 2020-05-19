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

    def test_menu_calls_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'Test Blog Title', 'Test Author', 'q')
            with patch('app.ask_create_blog') as mocked_ask_create_blog:
                app.menu()
                mocked_ask_create_blog.assert_called_once_with()

    def test_menu_calls_print_blogs(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('l', 'q')
            with patch('app.print_blogs') as mocked_print_blogs:
                app.menu()
                mocked_print_blogs.assert_called_with()

    def test_menu_calls_ask_read_blog(self):
        b = Blog('Test', 'Test Author')
        app.blogs = {'Test': b}

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('r', 'Test Title', 'q')
            with patch('app.ask_read_blog') as mocked_ask_read_blog:
                app.menu()
                mocked_ask_read_blog.assert_called_once_with()

    def test_menu_calls_ask_create_post(self):
        b = Blog('MyNote', 'Nat')
        b.create_post('Programming Tips', 'Be Lazy!!')
        b.create_post('Work Tips', 'Work Hard...')
        target_post = b.posts[0]

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('p', 'MyNote', 'Programming Tips', 'Be Lazy!!', 'q')
            with patch('app.ask_create_post') as mocked_ask_create_post:
                app.menu()
                mocked_ask_create_post.assert_called_once_with()

    def test_menu_initial_calls_print_blogs(self):
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
        with patch('builtins.input', return_value='Test'):
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

    def test_ask_create_post(self):
        b = Blog('MyNote', 'Nat')
        b.create_post('Programming Tips', 'Be Lazy!!')
        b.create_post('Work Tips', 'Work Hard...')
        target_post = b.posts[0]

        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('MyNote', 'Programming Tips', 'Be Lazy!!')
            with patch('blog.Blog.create_post') as mocked_create_post:
                app.ask_create_post()
                mocked_create_post.assert_called_with(target_post.title, target_post.content)
