import psycopg2
from config import config

def create_table():
   sql = """CREATE TABLE phonebook(
            contact VARCHAR(20),
            tel_number VARCHAR(20),
            tel_connection VARCHAR(20),
            email VARCHAR(50),
            relationship VARCHAR(50),
            PRIMARY KEY(tel_number)
            );
         """

   conn = None

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cursor = conn.cursor()
      cursor.execute(sql)
      cursor.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

if __name__ == '__main__':
   create_table()
