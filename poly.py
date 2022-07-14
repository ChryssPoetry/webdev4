#polymorphism in python

class Father:
    def Tvehicle(self):
        print("CYCLE")
class Son(Father):
    def Tvehicle(self):
        print("bike")

obj = Son()
print(obj.Tvehicle())

#kylieyying on polymorphism => OOP concept for conciseability and flexibility

#inheritance => creating new classes (child) off from already existing class (parent class)

class Dog:

    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_walk(self):
        return True

    def bark(self):
        return "woof"

class Samoyed(Dog):
    #initiating the Parent 
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)
        self.name = name
    def likes_walk(self):
        return True
 

class Poodle(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def fetch_ability(self):
        if self.age > 2:
            return 8
        elif self.age >10:
            return 10
        else:
            return 7
    def bark(self):
        return "boof! boof!"


    

class Goldenretriever(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

class Goldendoodle(Poodle, Goldenretriever): #multiple inheritance
    def __init__(self, name, age, friendliness):
        super().__init__(name, age,friendliness)
       
#lots of repetition, thus we create a super-class =>Dog

samy = Samoyed("samy", 2, 10)
goldie = Goldendoodle("goldie", 2, 10)

print(goldie.bark())
# print(goldie.likes_walk())

# print(goldie.fetch_ability())

#polymorphism, the concept of overiding a base class and giving it a new function
#oop with python engineer