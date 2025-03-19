import datetime
import mysql.connector

__cnx = None

def get_sql_connection():
  print("Establishing mysql connection!")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='password', database='grocery_store')

  return __cnx

