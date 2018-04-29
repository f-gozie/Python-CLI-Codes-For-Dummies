'''class string:
    def getstring(self, name):
        self.name = input("Name:")
        
    def printstring(self, prnt):
        self
        '''
'''class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
r = rectangle(3, 4)
print('area: ', r.area())
'''
class account(object):
    def __init__(self, deposit, withdraw, inquiry):
        self.deposit = deposit
        self.withdraw = withdraw
        self.inquiry = inquiry
    def deposit(self):
        print("You deposited: ", self.deposit)
    def withdraw(self):
        print("You just withdrew: ", self.withdraw)
    def inquiry(self):
        print("You have %s left in your account:" %(self.inquiry))
a = account

class accountupgrade(account):
    