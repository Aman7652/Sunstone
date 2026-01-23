
f = open("/Users/amankesarwani/Desktop/Python/File I:O/myfile.txt")

print(f.read())
f.close()

#we have another way where close() can't needed

with open("/Users/amankesarwani/Desktop/Python/File I:O/myfile.txt") as f:
    print(f.read( ))
