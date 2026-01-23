class calculater:
    def __init__(self,a):
        self.a=a
        
    def square(self):
        print(f"Square:{self.a**2}")
        
    def Cube(self):
        print(f"Cube:{self.a**3}")

    def SquareRoot(self):
        print(f"Cube:{self.a**1/2}")

a=int(input("Enter no:"))
result=calculater(a)
result.square()
result.Cube()
result.SquareRoot()