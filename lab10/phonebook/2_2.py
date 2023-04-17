import psycopg2
from config import config


def enter_contacts(name,number,connection,email,relation):

   sql = """
         INSERT INTO phonebook(contact, tel_number, tel_connection, email, relationship)
         VALUES (%s, %s, %s, %s, %s); 
         """

   conn = None

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cursor = conn.cursor()
      cursor.execute(sql, (name,number,connection,email,relation,))
      cursor.close()
      conn.commit()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()


name,number,connection,email,relation = map(str,input().split())

if __name__ == '__main__':
   enter_contacts(name,number,connection,email,relation)
