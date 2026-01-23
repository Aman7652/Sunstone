class Company:
    Company_Name="Microsoft"
    Salary=7000000

    def __init__(self,Name,Post):
        self.Name=Name
        self.Post=Post

Emp_1=Company ("Aman kesarwani","Data Scientist")
print(f"Company_Name: {Emp_1.Company_Name}, Name: {Emp_1.Name}, Post: {Emp_1.Post}, Salary:{Emp_1.Salary} ")