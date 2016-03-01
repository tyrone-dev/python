__author__ = 'tyronevb'

def add_integers(*list):
    sum = 0
    for num in list:
        sum += num
    return sum

def display_sum(*args):
    a = ', '.join(map(str, args))
    print "The sum of: " + a + " is {}".format(add_integers(*args))
    return 1

numbers = [1, 2, 3, 4, 5]

display_sum(*numbers)

'''
side bar:

def func(*args):
    # this function expects a variable number of arguments

def func2(list):
    # this function expects a list

# calling these:


func(*numbers)  # note *numbers to unpack the list

func2(numbers)  # no * - passes a list

# a list counts as one arg!!

'''