MENU_PROPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, "q" to quit'

blogs = dict()


def menu():
    print_blogs()
    selection = input(MENU_PROPT)


def print_blogs():
    for key, blog in blogs.items():
        print('- {}'.format(blog))
