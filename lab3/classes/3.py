class Shape:
    def __init__(self, number,number1):
        self.number=number
        self.number1=number1
    def Square(self):
        print(int(self.number)*int(self.number1))

class Rectangle(Shape):
    def __init__(self, number,number1):
        Shape.__init__(self,number,number1)

a=input().split()

area=Rectangle(a[0],a[1])
area.Square()
