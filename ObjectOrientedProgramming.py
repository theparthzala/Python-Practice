class test:
    def __init__(self,name,age,hobby): #The __init__() function is called automatically every time the class is being used to create a new object.
        self.name=name
        self.age=age
        self.hobby = hobby
    def display(self):
        print("My name is ",self.name)
        print("My hobby is ",self.hobby)
        print("My age is ",self.age)
obj1= test("Parth",23,"Football")
# obj1.display()
#Bank account project

class account:
    account_number=12345
    balance=0
    def __init__(self,balance,deposite):
        self.balance=balance
        self.deposite=deposite
    def current_balance(self,balance,deposite):
        balance=balance+deposite
        