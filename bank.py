
def deposte(depositramount):
    if depositramount<=0:
        print("your amount must be >=1")
        return 0
    else:
        return depositramount
    
def withdraw(amount,withdrawamount):
    if withdrawamount<=amount:
        return withdrawamount
    else:
        print("inssfesiant amount")
        return 0
def check_balnece(amount):
    print(f"your amount is {amount}")

def run(amount):
    while True:
        print("1) deposite")
        print("2) withdrawamount")
        print("3)checkamount")
        print("4) exit")
        otp=input("enter your choise:")
        if otp=="1":
            depositramount=float(input("enter deposite amount:"))
            amount+=depositramount
            print(f"deposite {depositramount} add succecss fully")
            input("please enter value to continue")

        elif otp=="2":
            withdrawamount=float(input("enter withdraw amount:"))
            amount-=withdraw(amount,withdrawamount)
            print(f"amount ${withdrawamount} withdraw succesfully")
            input("please enter value to continue:")

        elif otp=="3":
            check_balnece(amount)
            print("click enter button to continue:")

        elif otp=="4":
            print("thanks for visting")
            break
        else:
            print("valid")

amount=0.0
my_pin=1234
chance=0
while True:
    pin=int(input("enter pin:"))
    if (pin==my_pin):
        run(amount)
        break
    else:
        chance+=1
        if chance<=3:
            print("incorrect pin. please try again")
        else:
            print("try after 1 hour")
            break

