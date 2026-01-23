class Employee:
    name="Aman Kesarwani"# This is a class Attribute
    Post="Data Scientist"
    Salary=2400000

    def __init__(self, name, salary, post):# dunder method which is Automatically called 
        self.name=name
        self.Salary=salary
        self.Post=post
        print(f"I Am The King")

    def getinfo(self):
        print(f"language :{self.Post}, salary:{self.Salary}")

    @staticmethod
    def getoff():
        print("God father")


call=Employee("Sharad", 5000000, "Data Scientist Expert")
call.Empid=342 # This is an Instance Attribute
# call.Post="Data Analyst" # instance Attribute,take preference over the class attributes during assignment & retrieval
print(f"Name:{call.name}, Post:{call.Post}, Salary:{call.Salary}, Empid:{call.Empid}")

# call.getinfo()
# call.getoff()