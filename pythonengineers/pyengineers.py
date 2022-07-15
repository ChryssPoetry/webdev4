#Objects
#classes are use for more complex data structures, contains functions that describes the function of the an object



#classes with python engineers
class SoftwareEngineers:
    #Classs attributes
    alias = "KEYBOARD MAGICIANS"
    #dunder methods
    def __init__(self, position, name, age, level, salary): #special method for initializing the class
        # instance attributes
        self.position = position
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary
    def __str__(self): #when we want to return a string
        information = f" these are the informations \n name = {self.name}\n, age = {self.age}\n, position = {self.position}\n, level = {self.level}\n, salary = {self.salary}"
        return information


    def code(self):
        print(f"{self.name} is writing code")

    @staticmethod # => adding a decorator
    def entry_salary(age):
        if age < 25:
            return 5000
        if age < 30:
            return 7000
        return 9000


    def code_in_language(self, language):
        print(f"{self.name} is writing codes in {language}")

    def information(self):
        information=f" these are the informations \n name = {self.name}\n, age = {self.age}\n, position = {self.position}\n, level = {self.level}\n, salary = {self.salary}"

    

# four principles of object oriented programming
#inheritance
#one class taking the attributes and methods of another class
class Employee:
    def __init__(self, name, position, age, salary):
        self.name = name
        self.position = position
        self.age = age
    
        self.salary = salary
        
    
class Engineers(Employee):
    def __init__(self, name, position, age, salary,level):
        super().__init__(name, position, age, salary)
        self.level =level
class Designers(Employee):
    def __init__(self, name, position, age, salary, level):
        super().__init__(name, position, age, salary)
        self.level = level



#polymorphism
#abstraction
#encapsulation => instance variables are kept private, only available to the class, not outside the class
class Software_engineers:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None # underscore means private, accessible only internally
        self.__reallyPrivate = 5000
        self._no_of_bugs_solved = 0
    #getter
    def get_salary(self):
        return self._salary
    
     #setter   
    def set_salary(self, base_salary):
        self._salary = self._calculate_salary(base_salary)

    def codes(self):
        self._no_of_bugs_solved += 1
    def _calculate_salary(self, base_salary):
        if self._no_of_bugs_solved < 10:
            return base_salary
        if self._no_of_bugs_solved > 100:
            return base_salary * 2
        return base_salary * 3
     

se = Software_engineers("chryss", 12)
for i in range(70):
    print(se.codes())
se.set_salary(6000)
print(se.get_salary())



# se1 = SoftwareEngineers("engineer", "cynthia",23,"senior", 5000)# an instance of the class
# # print(se1.code_in_language("MySQL"))
# # print(se1.code())
# # print(se1.information())

# print(SoftwareEngineers.entry_salary(29))
# #with decorators, one can not access the self attribute
