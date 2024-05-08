import mysql.connector
from SAVING import take_value


def create_database(date, payment, cost, product):
    try:
        mycursor.execute(
            "CREATE TABLE Trackers (Date VARCHAR(255), Payment VARCHAR(50), Cost int UNSIGNED, Product VARCHAR(255), id int PRIMARY KEY AUTO_INCREMENT)"
        )
    except:
        mycursor.execute(
            "INSERT INTO Trackers (Date, Payment, Cost, Product) VALUES (%s, %s, %s, %s)",
            take_value(date, payment, cost, product),
        )
        mydb.commit()
    else:
        mycursor.execute(
            "INSERT INTO Trackers (Date, Payment, Cost, Product) VALUES (%s, %s, %s, %s)",
            take_value(date, payment, cost, product),
        )
        mydb.commit()
        

def show_data():
    mycursor.execute("SELECT * from Trackers")
    for x in mycursor:
        print(x)
    

def delete_data():
    mycursor.execute(f"DELETE FROM Trackers WHERE id ORDER BY id DESC LIMIT 1")
    mydb.commit()


mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="project_database"
)
mycursor = mydb.cursor()



