#Database Management Banking
import mysql.connector as sql

mydb = sql.connect(
            host="localhost",
            user="root",
            passwd="Yash@123",
            database="bank"
)

cursor = mydb.cursor()

def db_query(str):
    cursor.execute(str)
    result = cursor.fetchall()
    return result

def createcustomertable():
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS bank_customers
                (username VARCHAR(20) NOT NULL,
                password VARCHAR(20) NOT NULL,
                name varchar(20) NOT NULL,
                age INTEGER NOT NULL,
                city VARCHAR(20) NOT NULL,
                balance INTEGER NOT NULL,
                account_number INTEGER NOT NULL,
                card_number VARCHAR(16) )
    ''')

mydb.commit()

if __name__ == "__main__":
    createcustomertable()