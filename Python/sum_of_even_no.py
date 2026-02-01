sum=0
for i in range(1,51):
    if i%2==0:
        print(i,end=" ")
        sum+=i
print(f"\nSum:{sum}")

print("\nWith while")
i=1
sum2=0
while i<51:
    if i%2==0:
        print(i,end=" ") 
        sum2+=i  
    i+=1
print(f"\nSum:{sum2}")
