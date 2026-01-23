

with open("myfile.txt")as f:
   file= f.read()
   
content=file.replace("donkey","######")

with open("myfile.txt","w")as f:
     f.write(content)