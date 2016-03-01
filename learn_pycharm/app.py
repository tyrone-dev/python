from random import choice

__author__ = 'tyronevb'


# investigate live templates in PyCharm - CTRL + j
# alt + enter - code intentions: i.e. on main to create main function
# use imports and then code intentions will complete the imports automatically
# CTRL + q: view inline documentation
# refactoring ctrl, atl, m
# refactor this ctr, alt, shift, t
# language injection - not working?

class Person:

    def __init__(self, name):
        self.greeting = "Hello {name}"
        self.name = name

    # python special method
    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name=self.name)


def main():
    people = [
        Person('Harry'),
        Person('Bob'),
        Person('Cow')
    ]
    person = choice(people)
    print person
if __name__ == '__main__':
    main()
