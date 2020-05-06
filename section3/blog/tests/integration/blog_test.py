#!/usr/bin/python
# coding: utf-8
import unittest
from blog import Blog
from post import Post


class BlogTest(unittest.TestCase):
    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = [Post('', '')]
        expected_json = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': '', 'content': ''
                }
            ]
        }
        self.assertEqual(expected_json, b.json())

    def test_json_one_post(self):
        b = Blog('Test', 'Test Author')
        b.posts = [Post('Post Title', 'Post Content')]
        expected_json = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Post Title',
                    'content': 'Post Content'
                }
            ]
        }
        self.assertEqual(expected_json, b.json())

    def test_json_two_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = [Post('Post Title', 'Post Content'), Post('Foo', 'Bar')]
        expected_json = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Post Title',
                    'content': 'Post Content'
                },
                {
                    'title': 'Foo',
                    'content': 'Bar'
                }
            ]
        }
        self.assertEqual(expected_json, b.json())
