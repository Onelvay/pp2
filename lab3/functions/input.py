class Abay:
    def __init__(self, name):
        self.ima=name
    def printString(self):
        print(self.ima)
def getString():
        person=input()
        return person

person=Abay(getString())
person.printString()

