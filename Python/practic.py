# problem 1

# def greatest(num1,num2,num3):
#     if(num1>num2 and num1>num3):
#         print("num1 is greatest:",num1)

#     elif(num2>num1 and num2>num3):
#         print("num2 is greatest:",num2)

#     elif(num3>num1 and num3>num2):
#         print("num3 is greatest:",num3)


# num1=int(input("enter no1:"))
# num2=int(input("enter no2:"))
# num3=int(input("enter no3:"))
# greatest(num1,num2,num3)

# problem 2
# celsius to feranhite

def conversion(c):
    f= (c * (9/5))+ 32
    return f

c= float (input("Enter tem in celsius:"))
temp=conversion(c)
print(f"Tem in feranheit: {temp}")
