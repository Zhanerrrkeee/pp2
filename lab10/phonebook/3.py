import psycopg2
from config import config

def update_phone(contact, number):
   sql = """
      UPDATE phonebook
      SET tel_number = %s
      WHERE contact = %s
   """

   conn = None
   updated_rows = 0

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      cur.execute(sql, (number, contact))

      updated_rows = cur.rowcount

      conn.commit()

      cur.close()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()
   
   return updated_rows


def update_contact(contact, number):
   sql = """
      UPDATE phonebook
      SET contact = %s
      WHERE tel_number = %s
   """

   conn = None
   updated_rows = 0

   try:
      params = config()
      conn = psycopg2.connect(**params)
      cur = conn.cursor()
      cur.execute(sql, (contact, number))

      updated_rows = cur.rowcount

      conn.commit()

      cur.close()
   except (Exception, psycopg2.DatabaseError) as error:
      print(error)
   finally:
      if conn is not None:
         conn.close()
   
   return updated_rows


choose = input('What do you want to change?\nphone or contact?\n')

if choose == 'phone':
   contact = input('Previous contact? ==>  ')
   number = input('New number ==>  ')
elif choose == 'contact':
   number = input('Previous number? ==>   ')
   contact = input('New contact ==> ')
else:
   print('Error!')
   exit()

if __name__ == '__main__':
   if choose == 'phone':
      update_phone(contact, number)
   else:
      update_contact(contact,number)
