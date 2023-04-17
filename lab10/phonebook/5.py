import psycopg2
from config import config

def delete_contacts(name):
   sql = "DELETE FROM phonebook WHERE contact = %s"

   conn = None

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      cur.execute(sql, (name,))

      conn.commit()
      cur.close()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()

name = input('Which contact do you want to delete? Type it:\n')

if __name__ == '__main__':
   delete_contacts(name)
