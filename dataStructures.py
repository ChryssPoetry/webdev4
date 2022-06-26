#data structures
one_dimensional = ["a", "b", "c", "d"]
matrix = [[1,2], [2,3],[4,5]] # two dimensional list
assesing = list(range(20))
print(assesing[::-2])
#list unpacking
numbers = [1,2,3]
first, second, third = numbers # assigning the values on the list to each the variables
#interested in a few values
grace = list(range(20))
love, peace, *others = grace
print(others)
#iterating through the list
for number in enumerate(grace): # enumerate returns the index, a tuple which cant be written on
    key, value = number
    print("key =" + str(key), "value ="+ str(value)) # using unpacking and loop


#adding to the list
assesing.insert(0,40)
print(assesing)
#one can access the object in a list through the dot notation

#removing stuffs at the end
print(assesing.pop())
#or at a given index
print(assesing.pop(19))


#sorting list, two parameters "keys" and "reverse"
assesing.sort(reverse=True)
print(assesing)

#sorting a list of tuple
items = [
    ("product1", 10),
     ("product2", 20),
      ("product3", 30),
       ("product4", 40),
        ("product5", 50),
         ("product6", 60)
      
]
#defining a function that python would use for sorting the list
# def sort_tuple(item):
#     return(item[0])


# items.sort(key=sort_tuple, reverse=True)
# print(items)
#single annonymous function we can pass to other functions
#using lambda function

items.sort(key=lambda item:item[0])
print(items) # definning function that we are gonna use only once as an argument

#mapping list
prices = []
for item in items:
    prices.append(f"${item[1]}")
print(prices)

#using the map function
products =list(map(lambda item:item[0], items))
print(products)

#filtering, naive implementation
filtered = []
for item in items:
    if item[1] > 10:
        filtered.append(item[1])

print(filtered)
# more faster implemtation
fast_filt= list(filter(lambda item: item[1] >= 10, items))
print(fast_filt)
#listing and mapping for folks from functional programming background
#same concept in python
prices_comprehension=[item[1] for item in items] #list comprehension
print(prices_comprehension)
products_comprehension = [item[0] for item in items if item[1] >=10]
print(products_comprehension)
#zip function, combining two list that be a tuple
cars = ["tesla", "audi", "mercedes", "camry", "mini copper"]
models = [2012, 2013, 2015, 2016, 2022]
cars_and_model = list(zip(cars, models))
print(cars_and_model)
#stacks, last in first out => data structure
browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

browsing_session.pop()

#using the append and pop to build a browser like function

#queue => first in first out
from collections import deque
from pprint import pprint

carsB = deque(cars_and_model)
carsB.popleft()
print(carsB)

#tuples => read only list
#swapping two variables
x= 10
y =11
x,y =y,x
print("x", x)
print("y", y)

#arrays takes less memory and performs a little bit faster than arrays
#dictionary, used

dictionaryCars = dict(cars_and_model)
print(dictionaryCars)

dictionary_comprehension = {price:prices[1] for price in prices}
print(dictionary_comprehension)
#generator expressions
from sys import getsizeof
values = (x*2 for x in range(20))
print(values)
print(getsizeof(values))

#exercise
#getting a dictionary, storing it in a list, sorting it and return the zeroeth index
sentence = "most common interview questions"
char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] +=1
    else:
        char_frequency[char] = 1
pprint(char_frequency)
char_frequency_sorted = sorted(char_frequency.items(), key =lambda kv:kv[1], reverse =True)
print(char_frequency_sorted[0])
