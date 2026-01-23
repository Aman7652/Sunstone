class Employee:
    name="Aman Kesarwani"# This is a class Attribute
    Post="Data Scientist"
    Salary=2400000


call=Employee()
call.Empid=342 # This is an Instance Attribute
call.Post="Data Analyst" # instance Attribute,take preference over the class attributes during assignment & retrieval
print(f"Name:{call.name}, Post:{call.Post}, Salary:{call.Salary}, Empid:{call.Empid}")