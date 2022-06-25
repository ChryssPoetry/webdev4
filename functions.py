#python functions, reuseable chuncks of code
def greet(first_name, last_name):
    print(f"hello {first_name} {last_name}")

greet("franklin", "nwafor")
#types of functions
# 1- ones that performes a task
#1- one that calculates and returns a value
def get_greet(firstname, lastname):
    full_name = f"{firstname} {lastname}"
    return f"hello {full_name}"
print(get_greet("victoria", "petrenko"))
#all functions return none, unless when used specifically

def increment(number, by):
    return number + by

odd = increment(0, 1)
even = increment(0, 2)

print (odd)
print(even)

#using default values,
#args, multiple args one asterick

def multiply(*numbers):
    total = 1
    for number in numbers:
        total*=number
    return total
print(multiply(2,3,4,5))

#double asterick
#let us save information about users

def save_users(**users):
    print(users)
save_users(id=1, name = "john", stack = "mern")

#fizzbuzz algorithm
def fizzBuzz(input):
    if (input % 3 ==0 )and (input % 5 ==0):
        return "FIZZBUZZ"
    if input % 3 ==0:
        return "FIZZ"
    if input % 5 ==0:
        return "BUZZ"
    return input

    
print(fizzBuzz(7))


