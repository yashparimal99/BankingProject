# Bank Services
from database import *
import datetime
import random
from tabulate import tabulate


class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        

   

    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")
    def custprofile(self): 
        temp = db_query(
            f"SELECT * FROM bank_customers WHERE username = '{self.__username}';")
        if temp:
            print("***ACCOUNT DETAILS***")
           

            print(f"Username : {temp[0][0]}")
            print(f"Password : {temp[0][1]}")
            print(f"Name : {temp[0][2]}")
            print(f"Age : {temp[0][3]}")
            print(f"City : {temp[0][4]}")
            print(f"Balance : {temp[0][5]}")
            print(f"Account Number : {temp[0][6]}")
            print(f"Card Number : {temp[0][7]}")

            print("-----------------------------------------------")
            
        else:
            print("Account details not availabe")
 
    def history(self):

         temp = db_query(
            f"SELECT * FROM {self.__username}_transaction WHERE account_number = '{self.__account_number}';")
         if temp:
             headers = ["Date Time", "Account Number", "Remark", "Amount"]
             table_data = [list(row) for row in temp]
             print(tabulate(table_data, headers, tablefmt="pretty"))
         


    def balanceequiry(self):
        temp = db_query(
            f"SELECT balance FROM bank_customers WHERE username = '{self.__username}';")
        print(f"{self.__username} Balance is {temp[0][0]}")

    def deposit(self, amount):
        temp = db_query(
            f"SELECT balance FROM bank_customers WHERE username = '{self.__username}';")
        test = amount + temp[0][0]
        db_query(
            f"UPDATE bank_customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
        self.balanceequiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")

    def withdraw(self, amount):
        temp = db_query(
            f"SELECT balance FROM bank_customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            test = temp[0][0] - amount
            db_query(
                f"UPDATE bank_customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
            self.balanceequiry()
            db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                     f"'{datetime.datetime.now()}',"
                     f"'{self.__account_number}',"
                     f"'Amount Withdraw',"
                     f"'{amount}'"
                     f")")
            print(
                f"{self.__username} Amount is Sucessfully Withdraw from Your Account {self.__account_number}")

    def fundtransfer(self, receive, amount):
        temp = db_query(
            f"SELECT balance FROM bank_customers WHERE username = '{self.__username}';")
        if amount > temp[0][0]:
            print("Insufficient Balance Please Deposit Money")
        else:
            temp2 = db_query(
                f"SELECT balance FROM bank_customers WHERE account_number = '{receive}';")
            if temp2 == []:
                print("Account Number Does not Exists")
            else:
                test1 = temp[0][0] - amount
                test2 = amount + temp2[0][0]
                db_query(
                    f"UPDATE bank_customers SET balance = '{test1}' WHERE username = '{self.__username}'; ")
                db_query(
                    f"UPDATE bank_customers SET balance = '{test2}' WHERE account_number = '{receive}'; ")
                receiver_username = db_query(
                    f"SELECT username FROM bank_customers where account_number = '{receive}';")
                self.balanceequiry()
                db_query(f"INSERT INTO {receiver_username[0][0]}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer From {self.__account_number}',"
                         f"'{amount}'"
                         f")")
                db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                         f"'{datetime.datetime.now()}',"
                         f"'{self.__account_number}',"
                         f"'Fund Transfer -> {receive}',"
                         f"'{amount}'"
                         f")")
                print(
                    f"{self.__username} Amount is Sucessfully Transaction from Your Account {self.__account_number}")
                

  









     
            
       
    

        
      

        
            


      
        
                      
                
        
                
                
                
            
         
            
           
               
           