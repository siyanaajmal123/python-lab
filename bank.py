class Bankac:
    def getData(self,name,acno,actype):
        self.name=name
        self.acno=acno
        self.actype=actype
        self.bal=0
        #self.withd=withd
       
        
    def deposit(self):
        amount=int(input("enter the amount to be deposited"))
        self.bal+=amount

    def withdrawal(self):
        amount=int(input("enter the amount to withdraw"))
        if self.bal<amount:
            print("Insufficient balance")
        else:
            self.bal-=amount
            print(amount,"withdraw successfully")
            print("current balance",self.bal)
    def display_account(self):
        print("ACCOUNT DETAILS")
        print("------------------")
        print("Coustomer Name",self.name)
        print("Account Number",self.acno)
        print("Account Type",self.actype)

    def viewbal(self):
        print("Your current balance is:",self.bal)


ch=0
name=input("Enter the name:")
acno=input("Enter account number:")
actype=input("Enter account type:")
obj=Bankac()
obj.getData(name,acno,actype)
obj.display_account()

while ch!=4:
    print("1.Deposite")
    print("2.Withdraw")
    print("3.View balance")
    print("4.exit")
    ch=int(input("enter your choice"))
    if ch==1:
        obj.deposit()
    if ch==2:
        obj.withdrawal()
    if ch==3:
        obj.viewbal()
else:
    print("exited")
    
        
