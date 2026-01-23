
f = open("/Users/amankesarwani/Desktop/Python/File I:O/myfile.txt")

poem=f.read()

if "Twinkle" in poem:
    print("IT Contains Twinkle")
else:
    print("NO")

f.close() 