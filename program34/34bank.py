class Bank:
    def __init__(self, acc_no, name, type, bal):
      self.acc_no=acc_no
      self.name=name
      self.type=type
      self.bal=bal
    def deposit(self,amt):
        if amt<=0:
            print("it should be a positive number")
        else:
            self.bal+=amt
            print("your current balance is",self.bal)
    def withdraw(self,amt):
        if amt <= 0:
            print("it should be a positive number")
        elif amt > self.bal:
            print("insufficient balance")
        else:
            self.bal-=amt
            print("your current balance is",self.bal)
    def display(self):
        print(f"accounAt number:{self.acc_no}")
        print(f"account holder:{self.name}")
        print(f"account type:{self.type}")
        print("cuurent balance:",self.bal)

no=int(input("enter your account number:"))
name=(input("enter your name:"))
type=(input("enter your account type:"))
bal=float(input("enter your account balance:"))
usr1=Bank(no,name,type,bal)
while True:
   print("\n1.DEPOSIT\n2.WITHDRAW\n3.ACCOUNT INFORMATION\n4.EXIT")
   opt=int(input("enter your choice:"))
   if opt == 1:
       amt=int(input("enter amount:"))
       usr1.deposit(amt)
   elif opt == 2:
       amt=int(input("enter your withdrawal amount:"))
       usr1.withdraw(amt)
   elif opt == 3:
       usr1.display()
   elif opt == 4:
       exit(0)
   else:
    print("invalid choice")