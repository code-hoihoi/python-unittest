#!/usr/bin/python
# coding: utf-8
import unittest
from blog import Blog


class BlogTest(unittest.TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')
        posts = []

        self.assertEqual('Test', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual(posts, b.posts)  # one way of testing an empty list
        self.assertEqual(0, len(b.posts))  # another way of testing an empty list

    def test_repr(self):
        b1 = Blog('Test', 'Test Author')  # Test Case #1: no posts
        posts1 = []
        length1 = len(posts1)
        self.assertEqual(f"{b1.title} by {b1.author} ({length1} post{'s' if length1 > 1 else ''})", b1.__repr__())

        b2 = Blog('Threat of COVID-19', 'Anthony')  # Test Case #2: one post
        b2.create_post('Corona', 'Tony')
        length2 = 1
        self.assertEqual(f"{b2.title} by {b2.author} ({length2} post{'s' if length2 > 1 else ''})", b2.__repr__())

        b3 = Blog('My IT Blog', 'Nat')  # Test Case #3: two posts
        b3.create_post('Python', 'Jun')
        b3.create_post('Java', 'Taro')
        length3 = 2
        self.assertEqual(f"{b3.title} by {b3.author} ({length3} post{'s' if length3 > 1 else ''})", b3.__repr__())
