#handling exceptions
try:
    age = int(input("age: "))
    print(f"age = { age}")
    xfactor = 10/age
    print(f"xfactor = {xfactor}")
except (ValueError, ZeroDivisionError):
    print("you enterred an incorrect age")

try:
    file1=open("file1.txt")
    age = int(input("age"))
    print(age)
except (ValueError, ZeroDivisionError):
    print("incorrect value")
finally:
    file1.close()
#using the with open

with open("file4.txt") as file:
    print("file opened")
# contents with __enter__ and __exit__ supports content management systems
# the object can be used with the with statement
code1 = """ 

def calc_xfactor(age):
    if age <=0:
        raise ValueError("incorrect entry")
    return 10/age
try:
    calc_xfactor(-1)
except ValueError as error:
    print(error)
"""
# raising exception can be costly
#cost of raising an exception
from timeit import timeit # for calculating the time for executing python code
print(timeit(code1))
