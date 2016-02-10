#!/usr/bin/env python

"""
In depth look at Object Oriented Programming (OOP) using Python.

Also an attempt to get into the habit of using logging as opposed to print for debugs
"""

import logging

# logger
logger = logging.getLogger(__name__)
log_level = logging.DEBUG
logging.basicConfig(level=log_level,
        format='%(asctime)s %(name)s : %(message)s',
        datefmt='%d/%m/%Y %I:%M:%S %p'
        )

'''

now 'print' debug statements using: logger.debug(message)

also: logger.info
      logger.warning
      logger.error
      logger.critical

but, only messages == to log level and higher levels are displayed (i.e. debug displays all)

'''

# classes

'''
Theory:
    Class - user defined prototype for an object that has attributes that characterize any object of the class.
            attributes are data members (class variables and instance variables and methods
            Attributes are accessed by dot notaion

    Class Variable - variable that is shared by all instances of a class
                     defined within class but outside any of the class methods

    Data Member - a class or instance variable that holds data associated with a class and its objects

    Function Overloading - assignment of more than one behaviour to a particular function
                           behaviour varies by the types of objects or arguments involved

    Instance Variable - a variable that is defined inside a method and only belongs to the current instance of a class

    Inheritance - transfer of characteristics of a class to other classes that are derived from it

    Instance - an individual object of a certain class

    Instantiation - the creation of an instance of a class

    Method - a special kind of function that is defined in a class definition

    Object - a unique instance of a data structure that is defined by its class. Object comprises both data members and methods

    Operator Overloading - the assignment of more than one function to an operator

'''

# creating classes: use the 'class' statement

'''
class ClassName:
    'Optional class doc string'
    class_suite

    class doc string can be accessed by ClassName.__doc__

    class_suite consists of all the component statements defining class members, data attributes and functions

'''

class Employee:
    'Common base class for all employees'
    empCount = 0 # class variable - shared among ALL instances of the class (Access as Employee.empCount inside/outside of class)


    # __init__ method: class constructor or initialization method; called when you create a new instance of the class
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        #test = "Tempted" # not good
    # other methods are decalred as normal python functions; except that 'self' is always the first argument of a method
    # python adds the self arg to the list automatically when calling the method

    def displayCount(self):
        logger.info("Total Employees %d" %Employee.empCount)
        #logger.info(test)
    def displayEmployee(self):
        logger.info('Name: {}, Salary: {}'.format(self.name, self.salary))
    '''
    def __del__(self):
        # destructor: called when instance is about to be destroyed
        class_name = self.__class__.__name__
        logger.info('About to get rid of {}'.format(self.name))
        Employee.empCount -= 1 # decrement number of employees
        logger.info('{} removed'.format(class_name))
    '''

    '''
    Class Inheritance
        classes can be created by deriving them from a preexisting class
            - list parent class name in parenthesis after new class name

        child class inherits all the attributes of the parent class and can use these
        as if they were defined in child class

        child class can override data members and methods of the parent class

        class SubClassName(ParentClass1, ParentClass2 ...):
            'Optional documentation string'
            class_suite

    '''
class Parent: # define parent class
    parentAttr = 200

    def __init__(self):
        logger.info("Calling parent constructor")

    def parentMethod(self):
        logger.info("Calling parent method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        logger.info("Parent Attribute: {}".format(Parent.parentAttr))

    def myMethod(self):
        logger.info("This method is unique to the parent")

class Child(Parent): # define a child class inheriting from Parent Class
    def __init__(self):
        logger.info("Calling child constructor")

    def childMethod(self):
        logger.info("Calling child method")

    def myMethod(self):
        logger.info("This method is unique to the child")

# inheritence best demonstrated through interactive use

    '''
        A class can be derived from multiple parent classes.

        functions: issubclass(subclass, superclass) - returns True if given subclass is a indeed a subclass of superclass superclass
                   isinstace(obj, Class) - returns True if given obj is an instance of class Class or is an instance of a subclass of Class

        Parent or Superclass methods can be overridden: this can allow special functionality in subclasses:
            To overide a method use the same method name in both Parent and Child Class Definitions

        Base Overloading Methods
            Generic fucntions that can be overridden:
                __init__
                __del__
                __repr__
                __str__
                __cmp__

        Overloading Operators:
            allows new functions to be added to basic operators (+, -, *, / etc) based on data types acting on

            example below demonstrates overloading the addition operator to act on a vector of two elements as opposed to single operands. Note that the return type is an object!
    '''

class Vector: # define a vector class (x, y)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Vector (%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    '''
        Data Hiding
            object attributes may or may not be visible outside the class definition
            attributes named with '__' prefix are not directly visible to outsiders
        
        Python protects those members by internally changing the name to include the class name.
        Such attributes can be accessed as object._ClassName.__attrName()
    '''
    

class JustCounter:
    __ninjaCounter = 0

    def count(self):
        self.__ninjaCounter += 1
        logger.info('Ninja Counter = {}'.format(self.__ninjaCounter))


    
if __name__ == '__main__':

    # this code only executes if script is executed as the top level scritp (i.e. not if imported)

    '''
    Creating Instance Objects
        Instances of a class are created by calling the class using the class name and passing arguments required by the __init_method (note: self is automatically added)

    '''
    
    # list for keeping all our employees
    emps = []

    # create a few instances of the Employee class
    
    # note how the class variable (common to all instances of the class) is accessed before an instance is even created
    # simply use className.classVarName
    logger.info("Total employees: {}".format(Employee.empCount))

    # here we create a new instance of the employee class: pass args required by the __init__ method
    emp1 = Employee("Tyrone", 9000)
    emps.append(emp1) # append new employee to list

    # notice how the class variable (a counter of class objects in this case) changes after creating a class
    logger.info("Added New Employee. Total employees: {}".format(Employee.empCount))

    emp2 = Employee("Misa", 5000)
    emps.append(emp2)

    logger.info("Added New Employee. Total employees: {}".format(Employee.empCount))

    '''
    Accessing attributes
        an object's attributes are accessed using the dot operator with an object; attributes are class variables, instance variables, methods

    '''
    
    # display all employee details
    for emp in emps:
        emp.displayEmployee()

    
    # attributes can be added, removed and modified at any time:

    # adding attributes: obj_name.newAttrName = value
    emp1.bonus = 250000
    logger.info("Bonus for {} : {}".format(emp1.name, emp1.bonus))

    # modifying attributes
    emp1.salary = 15000
    logger.info("New salary for {} : {}".format(emp1.name, emp1.salary))

    # deleting attributes
    #del emp2.salary
    logger.info("Salary for {} has been removed".format(emp2.name))

    '''
    other functions for accesing attributes (instead of dot notation)
    getattr(obj, name) - returns value of specified attribute for given object
    hasattr(obj, name) - returns True if given object has attribute with name
    setattr(obj, name, value) - used to add or modify attributes (with name) given value to for a given object
    delattr(obj, name) - deletes attribute name for given object

    '''

    # Built in attributes
    '''
    every python class has a set of built-in attributes that can be accessed like any other attribute:
        __dict__ - dictionary containing class's namespace
        __doc__ - class doc string
        __name__ - Class name
        __module__ - module name in which the class is defined
        __bases__ - tuple containing the base classes in the order of occurance in the base clase list

    '''

    logger.info(Employee.__doc__)

    '''
    Garbage Collection
        Python deltes unneeded objects automatically to free up memory space. This is garbage collection.

        GC runs during program execution and is triggered when an object's reference count reaches zero.
            Reference count changes as the number of aliases that point to it changes

        An object's reference count increases when it is assigned a new name or placed in a container. Reference 
        count decreases when it is deleted, its reference is reassinged, or the reference goes out of scope

    '''
    
    # special method called destructor is invoked when an isntance is about to be destroyed
    # see above class definition

    # remove employee
    # del emp1

    


