
# function definition
# def avg():
#     a=int(input("Enter the no:"))
#     b=int(input("Enter the no:"))
#     c=int(input("Enter the no:"))
#     d=int(input("Enter the no:"))

#     average=(a+b+c+d)/4
#     print(f"Average of 4 no is {average}")

# function calling
# avg()

# function with aurgument
# def greet(name,v2):
#     print("Have a Good Day,"+ name)
#     print(v2)
#     return "hello"#return type function

# a=greet("Aman","enjoy") 
# print(a)


# function with default aurgument
# def greet(name,v2="Thank you"):
#     print("Have a Good Day,"+ name)
#     print(v2)
#     return "hello"

# a=greet("Aman","enjoy") 
# print(a) 


# recursion
# funtion calling it self until the problem get solved

def factorial(n):
    if (n==1 or n==0):
        return 1
    return n * factorial(n-1)

n=int(input("Enter No:"))
fact=factorial(n)
print(f"Factorial of {n} is {fact}")