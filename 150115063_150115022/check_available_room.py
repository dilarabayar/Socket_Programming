import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
def check_available_room(string):
 print("http",string)
 try:
  connection = psycopg2.connect(user="postgres",password="123",host="127.0.0.1",port="5433",database="postgres")
  cursor = connection.cursor()
  print(connection.get_dsn_parameters(), "\n")
  cursor.execute("SELECT version();")
  record = cursor.fetchone()
  print("You are connected to - ", record, "\n")

 except (Exception, psycopg2.Error) as error:
  print("Error while connecting to PostgreSQL", psycopg2.Error)
 return