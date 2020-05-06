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

    def test_repr_no_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = []
        self.assertEqual("Test by Test Author (0 post)", b.__repr__())

    def test_repr_one_post(self):
        b = Blog('Threat of COVID-19', 'Anthony')
        b.posts = ['Corona']
        self.assertEqual("Threat of COVID-19 by Anthony (1 post)", b.__repr__())

    def test_repr_two_posts(self):
        b = Blog('My IT Blog', 'Nat')
        b.posts = ['Python', 'Java']
        self.assertEqual("My IT Blog by Nat (2 posts)", b.__repr__())
