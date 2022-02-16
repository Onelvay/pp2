class bank:
    def __init__(self,owner, balance):
        self.owner=owner
        self.balance=balance
        self.deposit=0
    def withdraw(self):
        print("сколько денег хотите вывести? ")
        x=int(input())
        if(x>self.balance):
            print("недостаточно средств")
        else:
            self.balance-=x
            print("остаток баланса: ", self.balance)
    def deposit1(self):
        print("сколько денег вы хотите положить в депозит?")
        x=int(input())
        self.balance-=x
        self.deposit+=x
        print("денег в депозите:" , self.deposit)

class Account(bank):
    def __init__ (self, owner,balance):
        bank.__init__(self, owner, balance)
    



name=input()
balance=int(input())
cod=Account(name, balance)
cod.deposit1()
cod.withdraw()

