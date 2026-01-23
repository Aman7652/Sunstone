f = open("/Users/amankesarwani/Desktop/Python/File I:O/1file.txt")
lines=f.readlines()#use to read and output in the form of list 
print(lines,type(lines))
f.close()


f = open("/Users/amankesarwani/Desktop/Python/File I:O/1file.txt")
line=f.readline() #use to read only one line
print(line)

line1=f.readline()
print(line1)
f.close()