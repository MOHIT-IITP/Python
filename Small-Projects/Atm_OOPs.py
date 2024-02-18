import getpass
import os
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
        print(f"Name: {self.name}")
        print(f"Age: {self.age}.")
        print(f"Account No: {self.account_no}.")
        print(f"Balance: {self.balance}. ")
        print(f"Mobile No. :{self.mobile_no}" )
        print("Current Pin ",self.pin )
    
    def deposit(self,amount):
        acn=str(input("Enter Account No: "))
        if(str(self.account_no)==str(acn)):
            new=self.balance+amount
            print(f"Available Balance:  {new}")
        else:
            print("************************")
            print("Incorrect Account Number")
            print("************************")

    def name_change(self):
        acc1=str(input("Enter Account No : "))
        if str(self.account_no)==str(acc1):
            newname=str(input("Enter  New Name: "))
            newname_1=str(input("ReEnter New Name: "))
            if str(newname)==str(newname_1):
                self.name=newname
                print("New Name Is Changed Sucessfully.")
            else:
                print("New Name Not Matched")
        else:
            print("INCORRECT ACCOUNT NO. ")
        print(f"New Name : {self.name}")

    def withdraw(self):
        acc2=str(input("ReEnter Account No: "))
        if str(self.account_no)==str(acc2):
            pin1=str(input("Enter Pin Here: "))
            if str(self.pin)==str(pin1):
                amount=int(input("Enter Amount: "))
                if amount<=self.balance:
                    x=self.balance-amount
                    print(f"Your Available Balance is {x} ")
                else:
                    print("********************")
                    print("--------------------")
                    print("Insufficiant Balance")
                    print("--------------------")
                    print("********************")
            else:
                print("*************")
                print("INCORRECT PIN")
                print("*************")
        else:
            print("*********************")
            print("INCORRECT ACCOUNT NO.")
            print("*********************")

    def check_balance(self):
        print("ReEnter Account No: ")
        acc_n=str(input())
        if str(self.account_no) == str(acc_n):
            pin_1=str(input("Enter Pin Here: "))
            if str(self.pin)==str(pin_1):
                print(self.balance)
            else:
                print("*************")
                print("-------------")
                print("Incorrect Pin")
                print("-------------")
                print("*************")
        else:
            print("*********************")
            print("INCORRECT ACCOUNT NO.")
            print("*********************")

    def pin_change(self):
        print("ReEnter Account No. : ")
        acc=str(input())
        if str(self.account_no)==str(acc):
            pin_2=str(getpass.getpass("Enter Old Pin: "))
            if str(self.pin)==str(pin_2):
                newpin=str(getpass.getpass("Create New Pin: "))
                newpin_1=str(getpass.getpass("ReEnter New Pin: "))
                if len(newpin==4):
                    if str(newpin)==str(newpin_1):
                        self.pin=newpin
                    else:
                        print("Pin Not Matched")
                else:
                    print("**********************")
                    print("----------------------")
                    print("PIN MUST BE OF 4 DIGIT")
                    print("----------------------")
                    print("**********************")
                print("Your New Pin Is Created Sucessfully")
            else:
                print("*************")
                print("-------------")
                print("INCORRECT PIN")
                print("-------------")
                print("*************")
        else:
            print("**********************")
            print("----------------------")
            print("INCORRECT ACCOUNT N0. ")
            print("----------------------")
            print("**********************")

    def signin(self):
        print("****************************************************************************")
        print("*                                                                          *")
        print("*                        WELCOME TO MOHIT'S  ATM                           *")
        print("*                             ATM SYSTEM                                   *")
        print("****************************************************************************")

        a=str(input("Enter Account Number Here: "))
        n=str(input("Enter Name Here: "))
        p=str(getpass.getpass("Enter Pin Here: "))
        if(str(self.account_no)==str(a)):
            if(str(self.name)==str(n)):
                if(str(self.pin)==str(p)):
                    print("You Have Logged In Sucessfully")
                    x=int(input("'0': Get Detail \n'1': Balance  \n'2': Pin Change \n'3': Name Change \n'4' : Withdraw\n'5' : Deposit\n'6' : LogOut/SignOut"))
                    if(int(x)==1):
                        print(self.check_balance())
                    elif(int(x)==0):
                        print(self.detail())
                    elif(int(x)==2):
                        print(self.pin_change())
                    elif(int(x)==3):
                        print(self.name_change())
                    elif(int(x)==4):
                        print(self.withdraw())
                    elif(int(x)==5):
                        print(self.deposit())
                    elif(int(x)==6):
                        os.system("clear")
                        exit()
                else:
                    print("*************")
                    print("-------------")
                    print("INCORRECT PIN")
                    print("-------------")
                    print("*************")
            else:
                print("**************")
                print("--------------")
                print("INCORRECT NAME")
                print("--------------")
                print("**************")
        else:
            print("**********************")
            print("----------------------")
            print("INCORRECT ACCOUNT N0. ")
            print("----------------------")
            print("**********************")
    
a1= Atm("Mohit kumar",20,394,1234,9999,9876,1234567890)
# print(a1.deposit(1))
print(a1.withdraw())
# print(a1.signin())











