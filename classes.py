#classes, a class is a blueprint for creating new objects
#object is an instance of a class

#creating a class => pascal naming convention; first letter of every world should be uppercase
from operator import setitem


class Point:
    def __init__(self, x,y):
        self.x =x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    @classmethod # decorator, to extend the function to that of a class
    def zero(cls):
        return cls(0,0)
    

    
    def draw(self):
        print("draw")


#constructor, a new method that is called when a new object is created
#magic method are classed immediately when a new object is created

class  LessThan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
       
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

other = LessThan(110,20)
lessthan = LessThan(1,2)
# print(other == lessthan)
# print(other > lessthan)

#making class containers
class TagLoud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
       self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1
    #getting the tags through indexing
    def __getitems__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    def __len__(self):
        return len(self.__tags)
    def __iter__(self):
        return iter(self.__tags)

#kepping stuffs private add double underscore to the attribute __tags


cloud =TagLoud()
cloud.add("python")
cloud.add("Python")
cloud.add("python")
cloud["python"] = 10
#this only reads the number of a given tag


# private members
#adding __, can still be accessed by __dict__
print(cloud.__dict__)

#unpythonic code, not using the python features to the fullest potential
class Product:
    def __init__(self, price):
        self.price = price
    @property # converting an instance method to a class method
    def price(self):
        return self.__price
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("value cannot be less than zero")
        self.__price = value
        #pythonic codes
        
        
#inheritances, 
#to not repeat onself, inheritance or composition can be implemented
class Animal:
    def __init__(self):
        self.age = 1
        print("animal constructor")
    def eat(self):
        print("its a mammal")
class Mammal(Animal):
    def __init__(self):
        print("mammal constructor")
        self.weight = 1
        super().__init__()
        
    def walk(self):
        print("___")
    
class Fish(Animal):
    def swim(self):
        print("___")
   
#  Animal : parent or Base
# Mammal : child or base

#multi-level inheritance, limit inheritance to two levels
class Bird(Animal):
    def fly(self):
        print("fly")

#object class
# m = Mammal()
# print(m.age)

# print(m.age)
# print(m.weight)

#multiple base classes implementation

class Employee:
    def greet(self):
        print("Employee greet")

class Person:

    def greet(self):
        print("person greet")

class Manager(Employee, Person):
    pass

manager = Manager()
print(manager.greet())

#a good example of inheritance
#importing the abstract module with which we would decorate
from abc import ABC, abstractmethod
class InvalidOperationError(Exception):
    pass
class Stream(ABC):
    def __init__(self):
        self.opened = False
       
    def open(self):
        if self.opened:
            raise InvalidOperationError('invalid exception')
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError ("invalid operation")
        self.opened = False
    @abstractmethod
    def read(self):
        pass
    class FileStream(Stream):
        def read(self):
            print("reading data from a stream")
class NetworkStream(Stream):
    def read(self):
        print("reading data from a network")
class MemoryStream(Stream):
     def read(self):
        print("read the data")
   
#abstract base class; provides common code to its derivatives
stream = MemoryStream()
stream.open()