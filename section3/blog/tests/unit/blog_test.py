#!/usr/bin/python
# coding: utf-8
import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        posts_list = []

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual(posts_list, b.posts)  # one way of testing an empty list
        self.assertEqual(0, len(b.posts))  # another way of testing an empty list
