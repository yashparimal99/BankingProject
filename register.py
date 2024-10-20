#User Registration Signin Signup
from customer import *
from bank import Bank
import random

def SignUp():
    username = input("Create Username: ")
    
    temp = db_query(f"SELECT username FROM bank_customers where username = '{username}';")
    if temp:
        print("Username Already Exists")
        SignUp()
    else:
        print("Username is Available Please Proceed")
        password = input("Enter Your Password: ")
        name = input("Enter Your Name: ")
        age = input("Enter Your Age: ")
        city = input("Enter Your City: ")
        while True:
            account_number = random.randint(10000000, 99999999)
            card_number = "2030400" + ''.join(str(random.randint(0, 9)) for _ in range(9))

            temp = db_query(f"SELECT account_number FROM bank_customers WHERE account_number = '{account_number}' "
                    f"OR card_number = '{card_number}';")
            if temp:
                continue
            else:
                print(f"Your Account Number : {account_number}")
                print(f"Your Card Number : {card_number}\n")
                print("---------------------------------------")
                break
 
    
    cobj = Customer(username,password,name,age,city,account_number,card_number)
    cobj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
def SignIn():
    username = input("Enter Username: ")
    temp = db_query(f"SELECT username FROM bank_customers where username = '{username}';")
    if temp:
        while True:
            password = input(f"Welcome {username.capitalize()} Enter Password: ")
            temp = db_query(f"SELECT password FROM bank_customers where username = '{username}';")
            # print(temp[0][0])
            if temp[0][0] == password:
                print("Sign IN Succesfully")
                return username
            else:
                print("Wrong Password Try Again")
                continue
    else:
        print("Enter Correct Username")
        SignIn()