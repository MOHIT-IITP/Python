class Atm:
    balance=0
    def __init__(self,name,age,id,account_no,balance,pin,mobile_no):
        self.name=name
        self.age=age
        self.id=id
        self.account_no=account_no
        self.balance=balance
        self.pin=pin
        self.mobile_no=mobile_no


    def detail(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}.")
        print(f"Your Account no is {self.account_no}.")
        print(f"Your Balance is {self.balance}. ")
        print(f"Your Mobile no. is :{self.mobile_no}" )
        print("your pin is ",self.pin )
    
    def deposit(self,amount):
        new=self.balance+amount
        print(f"Your available Balance is:  {new}")

    def name_change(self):
        acc1=str(input("Enter your account no : "))
        if str(self.account_no)==str(acc1):
            self.name=str(input("Enter your  new name: "))
            print("New name is changed sucessfully.")
        print(f"Your new name is: {self.name}")

    def withdraw(self):
        acc2=str(input("Enter your account no: "))
        if str(self.account_no)==str(acc2):
            pin1=str(input("Enter your pin Here: "))
            if str(self.pin)==str(pin1):
                amount=int(input("Enter your amount: "))
                if amount<=self.balance:
                    x=self.balance-amount
                    print(f"Your available balance is {x} ")
                else:
                    print("Insufficiant Balance")

    def know_balance(self):
        print("Enter your account no: ")
        acc_n=str(input())
        if str(self.account_no) == str(acc_n):
            print(self.balance) 
        else:
            print("Sorry")

    def pin_change(self):
        print("Enter your account no: ")
        acc=str(input())
        if str(self.account_no)==str(acc):
            self.pin=str(input("Create your new pin: "))
            print("Your New pin is created sucessfully")
        else:
            print("Sorry")

    

a1= Atm("mohit kumar",20,394,123,9999,9876,1234567890)
print(a1.detail())
print(a1.deposit(1))
print(a1.withdraw())
print(a1.know_balance())
print(a1.pin_change())
print(a1.name_change())












