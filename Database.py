import mysql.connector
from SAVING import take_value

def create_database(mycursor):
  try:
      mycursor.execute("CREATE TABLE Trackers (Date VARCHAR(255), Payment VARCHAR(50), Cost int UNSIGNED, Product VARCHAR(255), id int PRIMARY KEY AUTO_INCREMENT)")
  except:
      mycursor.execute("INSERT INTO Trackers (Date, Payment, Cost, Product) VALUES (%s, %s, %s, %s)", take_value())
  else:
      mycursor.execute("INSERT INTO Trackers (Date, Payment, Cost, Product) VALUES (%s, %s, %s, %s)", take_value())
      
def delete_data(mycursor):
   mycursor.execute(f"DELETE FROM Trackers WHERE id ORDER BY id DESC LIMIT 1")


def main():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database = "project_database"
  )

  input = "0"
  mycursor = mydb.cursor()

  # 1 for Create & 0 for delete

  mydb.commit()

  mycursor.execute("SELECT * from Trackers")
 
  for x in mycursor:
     print(x)
 
main()


