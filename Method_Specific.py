### Object specific variable
##class Customer:
##    def deposit(self,amt):     #amt is local variables
##        print("Method specific variable",amt)   
##
##test=Customer()
##test.deposit(500)
##
### guess the output
##class Test:
##    a=100
##    def __init__(self):
##        self.b=200
##
##t=Test()
##print(t.b) #200
##print(t.a) #100
##t.a =777  
##print(t.a)  #777
##print(Test.a) #100

##
###Instance Method
##
##class Student:
##    def __init__ (self,name,marks):
##        self.name=name
##        self.marks=marks
##    def disp(self):
##        print('Hi',self.name,'your marks is',self.marks)
##
##
##j=Student("Harshi",100)
##j.disp()

### Class Specific Methods
##class Office:
##    no_holiday=10
##    @classmethod
##    def check(cls,branch):
##        print("Hi this year our",branch,"has",cls.no_holiday)
##
##
##Office.check("chennai")
##h=Office()
##h.check('Ban')


##
### Static Methods
##class cal:
##    @staticmethod
##    def add(n1,n2):
##        print('Result',n1+n2)
##
##cal.add(10,20)



import sys
class bank:
    bankname="IOB"
    def __init__(self,name,accno):
        self.name=
        self.accno=
    def deposit(self,amt):

    def withdraw(self,amount):
        pass
print("Welcome to",bank.bankname)
name=input("enter name")
accno=int(input("Enter accno"))
cust1=bank(name,accno)
while True:
    print('D-Deposit','W-Withdraw')















































