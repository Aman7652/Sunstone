
def table():
    for j in range(2,51):

        for i in range(1,11):
            with open(f"2table.txt","a")as f:
                table=f"{j}X{i}={j*i}\n"
                f.write(str(table))

        
        with open(f"2table.txt","a")as f:
            f.write("\n")

        j+=1
table()