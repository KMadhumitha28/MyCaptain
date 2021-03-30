import sqlite3

def connect(dbname):
  connection= sqlite3.connect(dbname)
  connection.execute("CREATE TABLE IF NOT EXITS OYO_HOTEL(NAME TEXT, ADDRESS TEXT, PRICE INT, AMENITIES TEXT, RATING TEXT)")

  print("table is created...!!")
  connection.close()


def insert_into_table(dbname,values):
  connection= sqlite3.connect(dbname)  
  connection.execute("INSERT INTO OYO_HOTEL (NAME, ADDRESS, PRICE, AMENITIES, RATING)  VALUES (?,?,?,?,?) ", values)
  

  connection.commit()
  connection.close()


def get_hotel_info(dbname):
  connection= sqlite3.connect(dbname)   
  curser= connection.cursor()
  curser.exeute("SELECT * FROM OYO_HOTEL")
   
  table_data= curser.fetchall()

  for r in table_data:
    print(r) 
