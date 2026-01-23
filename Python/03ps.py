from random import randint

class Train:

    def __init__(self,train_no):
        self.train_no=train_no

    def book(self, to,fro):
        print(f"Train No {self.train_no} is booking from {to} to {fro}")
        
    def stutus(self):
        print(f"Train No {self.train_no} is running on Time")
    
    def fare(self,to,fro):
        print(f"Train No {self.train_no} is booking   from Bording point{to} to {fro} ticket fare :{randint(500,7000)}")

    
call=Train(12304)
call.book("Prayagraj","Jaipur")
call.stutus()
call.fare("Prayagraj","Jaipur")