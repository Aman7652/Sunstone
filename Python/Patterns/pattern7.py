n=int(input("Enter n:"))
i=1
star=1
while(i<=n*2-1):
    j=1
    while(j<=star):
        print("*",end=" ")
        j+=1
    i+=1
    if(i<=n):
        star+=1
    else:
        star-=1
    print()