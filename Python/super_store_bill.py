while True:
    name=input("Enter Name:")
    mobile=int(input("Enter Number:"))
    total=0
    while True:
       price=int(input("Enter product price:"))
       quantity=int(input("Enter product Quantity:"))
       amount=price*quantity
       total+=amount
       rep=input("Want to add product:")
       if rep=="NO" or rep=="no":
            break;
    rep1=input("Add new Custumer:")
    if rep1=="NO" or rep1=="no":
            break;

print("-"*50)
print(f"Name:{name}")
print(f"Mobile No:{mobile}")
print(f"Total Amount To Be Paid:{total}")
print("-"*50)
print("*"*20,"Thank You","*"*20)