#!/usr/bin/python
# coding: utf-8

blogs = dict()  # the reason not using {} is to avoid the confusion with set (set is also written as {}).


def menu():
    """
    Show the users the available blogs.
    Let the user make a choice.
    Do something with that choice.
    Eventually exit.
    """
    print_blogs()


def print_blogs():
    """
    Print the available blogs.
    """
    for key, blog in blogs.items():
        print(f"- {blog}")
