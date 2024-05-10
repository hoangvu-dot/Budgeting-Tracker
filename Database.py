import mysql.connector
from SAVING import take_value, taking_month
import numpy as np


def create_databases(date, payment, cost, product):
    try:
        mycursor.execute(
            "CREATE TABLE Trackers (Date VARCHAR(255), Payment VARCHAR(50), Cost int UNSIGNED, Product VARCHAR(255))"
        )
    except:
        mycursor.execute(
            "INSERT INTO Trackers (Date, Payment, Cost, Product) VALUES (%s, %s, %s, %s)",
            take_value(date, payment, cost, product),
        )
        mydb.commit()


def show_data():
    mycursor.execute("SELECT * from Trackers")
    for x in mycursor:
        print(x)


def retrieve_data():
    mycursor.execute("SELECT * from Trackers")
    lst = [x for x in mycursor]
    return lst


def delete_data():
    mycursor.execute(f"DELETE FROM Trackers WHERE id ORDER BY id DESC LIMIT 1")
    mydb.commit()


def monthly_spend() -> int:
    mycursor.execute("SELECT Cost from Trackers")
    total = 0
    for x in mycursor:
        total += x[0]
    return total


def unique_item():
    mycursor.execute("SELECT Product, Cost from Trackers")
    item = {}
    for x in mycursor:
        if x[0] not in item:
            item[x[0]] = x[1]
        else:
            item[x[0]] += x[1]

    number_transaction = monthly_spend()
    for x in item:
        item[x] /= number_transaction
        item[x] *= 100

    return item

def reset_month():
    current_total = monthly_spend()
    current_month = 0
    mycursor.execute("SELECT Date FROM Trackers WHERE id ORDER BY id DESC LIMIT 1")
    for x in mycursor:
        current_month= taking_month(x[0])
        break

    try:
        mycursor.execute(
            "CREATE TABLE Month (month int UNSIGNED, value int UNSIGNED)"
        )
    except:
        mycursor.execute(
            "INSERT INTO Month (month, value) VALUES (%s, %s)", (current_month, current_total)
        )
    
    mycursor.execute("TRUNCATE Trackers")
    mydb.commit()


mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="project_database"
)
mycursor = mydb.cursor()


def main():
    ...

if __name__ == "__main__":
    main()
