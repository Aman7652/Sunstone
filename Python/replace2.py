words=["Gando","Donkey","Fuck-off"]

with open("myfile.txt") as f:
    content=f.read()

for word in words:
    content=content.replace(word,"#"*len(word))

with open("myfile.txt","w") as f:
    f.write(content) 