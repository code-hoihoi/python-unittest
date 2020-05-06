#!/usr/bin/python
# coding: utf-8


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"{self.title} by {self.author} " \
               f"({len(self.posts)} post{'s' if len(self.posts) > 1 else ''})"

    def create_post(self, title, author):
        self.posts.append({
            'title': title,
            'author': author
        })

    def json(self):
        pass
