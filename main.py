
from register import *
from bank import *

status = False

print("--------------------------------------------------------")
print("Welcome to Yash Banking Project\n")
while True:

    try:
        print("Choose your Banking Option \n 1. SignUp \n 2. SignIn \n")
        register = int(input("Choose Banking Option  : "))
        if register == 1 or register == 2:
            if register == 1:
                SignUp()
            if register == 2:
            
                user = SignIn()
                status = True
                break
        else:
            print("Please Enter Valid Input From Options")

    except ValueError:
        print("Invalid Input Try Again with Numbers")

account_number = db_query(
    f"SELECT account_number FROM bank_customers WHERE username = '{user}';")

while status:
    print(f"-----Welcome {user.capitalize()} Choose Your Banking Service-----\n")
    try:
        print("1. Account Details")
        print("2. Transaction History")
        print("2. Transaction History")
        print("3. Balance Enquiry")
        print("4. Cash Deposit")
        print("5. Cash Withdraw")
        print("6. Fund Transfer")
        print("7. Exit\n")
         


        facility = int(input("Choose Banking Facility  "))
        if facility >= 1 and facility <= 7:

             if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.custprofile()

             if facility == 2:
                 bobj = Bank(user, account_number[0][0])
                 bobj.history()
               
             elif facility == 3:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceequiry()
             elif facility == 4:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit  "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                        
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

             elif facility == 5:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw  "))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
             elif facility == 6:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number  "))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
             
                     
                 
                 
            
               
             elif facility == 7:
                print("Thanks For Using Banking Services")
                status = False
                print("\n--------------------------------------------")
        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue
