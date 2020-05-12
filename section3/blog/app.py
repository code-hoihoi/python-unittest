#!/usr/bin/python
# coding: utf-8
from blog import Blog
from post import Post

MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
blogs = dict()  # the reason not using {} is to avoid the confusion with set (An empty set is also initialized with {}).


def menu():
    """
    Show the users the available blogs.
    Let the user make a choice.
    Do something with that choice.
    Eventually exit.
    """
    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)

def print_blogs():
    """
    Print the available blogs.
    """
    for key, blog in blogs.items():
        print(f"- {blog}")


def ask_create_blog():
    title = input('Enter the blog\'s title: ')
    author = input('Enter the author\'s name: ')
    b = Blog(title, author)
    blogs[title] = b


def ask_read_blog():
    title = input('Enter the blog\'s title you wanna read: ')
    print_posts(blogs[title])


def print_posts(blog):
    for post in blog.posts:
        print_one_post(post)


def print_one_post(post):
    print(f"--- {post.title} --- \n\n {post.content} \n\n")


def ask_create_post():
    title = input('Enter the post\'s title: ')
    content = input('Enter the post\'s content: ')
    p = Post(title, content)

