#!/usr/bin/python
# coding: utf-8
import unittest
from post import Post


class PostTest(unittest.TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')

        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
