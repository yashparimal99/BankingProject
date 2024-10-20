
from register import *
from bank import *

status = False

print("--------------------------------------------------------")
print("Welcome to Yash Banking Project\n")
while True:

    try:
        print("Choose your Option \n 1. SignUp \n 2. SignIn \n")
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
    print(f"Welcome {user.capitalize()} Choose Your Banking Service\n")
    try:
        facility = int(input("1. Account Details\n"
                             "2. Balance Enquiry\n"
                             "3. Cash Deposit\n"
                             "4. Cash Withdraw\n"
                             "5. Fund Transfer\n"
                             "6. Exit\n "
                             ))
        if facility >= 1 and facility <= 6:

             if facility == 1:
                bobj = Bank(user, account_number[0][0])
                bobj.custprofile()

           
               
           
             elif facility == 2:
                bobj = Bank(user, account_number[0][0])
                bobj.balanceequiry()
             elif facility == 3:
                while True:
                    try:
                        amount = int(input("Enter Amount to Deposit"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.deposit(amount)
                        mydb.commit()
                        break
                        
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue

             elif facility == 4:
                while True:
                    try:
                        amount = int(input("Enter Amount to Withdraw"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.withdraw(amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
             elif facility == 5:
                while True:
                    try:
                        receive = int(input("Enter Receiver Account Number"))
                        amount = int(input("Enter Money to Transfer"))
                        bobj = Bank(user, account_number[0][0])
                        bobj.fundtransfer(receive, amount)
                        mydb.commit()
                        break
                    except ValueError:
                        print("Enter Valid Input ie. Number")
                        continue
             
                     
                 
                 
            
               
             elif facility == 6:
                print("Thanks For Using Banking Services")
                status = False
                print("\n--------------------------------------------")
        else:
            print("Please Enter Valid Input From Options")
            continue

    except ValueError:
        print("Invalid Input Try Again with Numbers")
        continue
