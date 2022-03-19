# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 14:43:38 2022

@author: oussama

POO:
    State: Attributes
    Behavior: methods
    Identity: a unique name to an object
"""

class Dog:
    
    #Class Variable:
    animal = "dog"  

    #Constructor:
    def __init__(self, name):
        
        #name is an attribute(Instance Variable)
        self.name = name
    
    #A method
    def say_hi(self):
        print("Hi my name is", self.name)
        
    #Destructor:
    def __del__(self):
        print("Destructor called")
        
#Instantiation
Rodger = Dog("Pitbull")

print(Rodger.name)
print(Rodger.animal)
Rodger.say_hi()
del Rodger
#Class Variables can be accessed using class name
print(Dog.animal)

"""
Self: Class methods must have an extra first parameter in the method definition
When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted 
by Python into MyClass.method(myobject, arg1, arg2)
"""

"""
Constructor: __init__ method
            used to initialized the object's state'
            executed at time of Object Creation
Types of constructors:
            Default constructor: One argument is a reference to the instance == self
            Parameterized Constructor: self + arguments
"""

"""
Instance Variables: unique to each instance
Class Variables: are for attributes and methods shared by all instances of the class
             Whose values is assigned in the class
"""

"""
Destructor ==> Not nedeed because python has a garbage collector
    that handles memory management automatically.
   is called after the programm ended or when all references to object are deleted 
"""

"""
Inheritance
in python 3.x : class person equivalent to class person(object)
object is root of all classes
"""

#Base == Super Class
class Person(object):
    
    #Constructor:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    
    def display(self):
        print(self.name)
        print(self.idnumber)
    
    #To get a name:
    def getName(self):
        return self.name
    
    #Check if a person is employee
    def isEmployee(self):
        return False

#Inherited or subclass
class Employee(Person):

    #constructor
    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post
        #invoking the parent constructor
        Person.__init__(self, name, idnumber)
    
    def isEmployee(self):
        return True    

emp = Person("oussama",1)
print(emp.getName(), emp.isEmployee())

emp = Employee("oumnia", 20000, 3000, "intern")
emp.display()

"""
If we dont invoke the __init__() of the parent class
then its instance variables would not available to the child class
"""

"""
Forms of inheratance:
        Single Inheritance: from only one parent
        Multiple Inheritance: inherits from multiple parents
        Multilevel inheritance: when we have a child and grandchild relationship 
        Hiearchical inheritance: more than one derived classes are created from a single base
        Hybrid inheritance: more than one type of inheritance
"""
print("*****************************************************")
class Base1(object):
    def __init__(self):
        self.str1 = "oussama"
        print("Base1")
        
class Base2(object):
    def __init__(self):
        self.str2 = "bougattaoui"
        print("Base 2")
    
class Derived(Base1, Base2):
    def __init__(self):
        #•Calling Constructor for Base1 and Base2
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")
    
    def printStr(self):
        print(self.str1, self.str2)


d = Derived()
d.printStr()

print("*****************************Multilevel inheritance************************")

class Base(object):
    
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        return self.name

class Child(Base):
    
    def __init__(self, name, age):
        Base.__init__(self, name)
        self.age = age
    
    def getAge(self):
        return self.age

class GrandChild(Child):
    
    def __init__(self, name, age, adress):
        Child.__init__(self, name, age)
        self.adress = adress
    
    def getAdress(self):
        return self.adress
    
gc = GrandChild("oussama", 22, "paris")
print(gc.getName(), gc.getAge(), gc.getAdress())


"""
Private members of parent class
we dont always want the instance variables of the parent
class to be inherited by the child class.
"""
print("*****************************Private Members***********************")

class C(object):
    def __init__(self):
        self.c = 21
        
        #private instance
        self.__d = 42

class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)

object1 = D()
#print(object1.d)#AttributeError has no attribute d
object2 = C()
#print(object2.d)#Cannot acces it directly / AttributeError has no attribute d

"""
Encapsulation: hide data
        to prevent accidental change ==> an object's variable
        can only be changed by an object's method ==> Private
        It describes the idea of wrapping data and the methods that work on data within one unit. 
A class is an example of encapsulation as it encapsulates all the data 
that is member functions, variables,...
"""

"""
Protected members:
    are those members of the class that cannot be accessed outside the class but can be accessed from within the class and its subclasses.
    
"""
class Base(object):
    def __init__(self):
        self._a = 2 #Protected member

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected membre", self._a)
        
        #modify the protected variable
        self._a = 3
        print("Calling modified protected member outside class:", self._a)

obj1 = Derived()
obj2 = Base()
#Calling a protected member from outside
print(obj1._a) #Can a ccess but shoul not be done due to convention
print(obj2._a)

"""
Private members:
   the class members declared private should neither be accessed outside the class nor by any base class.     
"""
print("*****************************Private Members***********************")
class Base:
    def __init__(self):
        self.a = "oussama"
        self.__c = "bougattaoui"

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("calling private member of base class")
        print(self.__c)

obj1 = Base()
#print(obj1.__c) #Attribute Error
#obj2 = Derived() #Attribute error also


"""
Polymorphism in python
    means having many forms
    The same function name(but different signature) being used for different types.
    Exemple : function len()
    lets us define methods int hte child class that have the same name as the methods in the parent class

Method ovverriding : is re-implementing a method in the child class.
"""
class Bird:
  def intro(self):
    print("There are many types of birds.")
     
  def flight(self):
    print("Most of the birds can fly but some cannot.")
   
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
     
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
     
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()
 
obj_bird.intro()
obj_bird.flight()
 
obj_spr.intro()
obj_spr.flight()
 
obj_ost.intro()
obj_ost.flight()
"""
Though we are using the name ‘obj’, any instantiated object will be able to be called into this function.
"""
class India():
    def capital(self):
        print("New Delhi is the capital of India.")
  
    def language(self):
        print("Hindi is the most widely spoken language of India.")
  
    def type(self):
        print("India is a developing country.")
  
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")
  
    def language(self):
        print("English is the primary language of USA.")
  
    def type(self):
        print("USA is a developed country.")
 
def func(obj):
    obj.capital()
    obj.language()
    obj.type()
  
obj_ind = India()
obj_usa = USA()
  
func(obj_ind)
func(obj_usa)

"""
Static variables for all objects ==> to make a class variable
    All var which are assigned a value in the class declaration are class variables
    and var rhat are assigned values inside methods are instance variables
    Class variables ==> can be access by the name of class or name of objects
    we canchange the class var for a specific object
    and if we use the class for changing the variable class will change the value for all objects that not change the class var for them selve 
"""