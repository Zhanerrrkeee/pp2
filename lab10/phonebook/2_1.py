import csv, psycopg2
from config import config

contact_list = [
   ('contact', 'tel_number', 'tel_connection', 'email', 'relationship'),
   ['mother', '8-707-977-38-08', 'Tele2', 'mother@gmail.com', 'mother'],
   ['brother', '8-707-184-31-19', 'Tele2', 'brother@gmail.com', 'sibling'],
   ['Merey', '8-707-862-28-90', 'Tele2', 'merey@gmail.com', 'friend'],
   ['father', '8-775-768-10-40', 'Activ', 'father@gmail.com', 'father'],
   ['Magzhan', '8-708-341-13-65', 'Altel', 'magzhan@gmail.com', 'relative'],
   ['Almat', '8-708-390-72-25', 'Altel', 'almat@gmail.com', 'friend'],
   ['Meirambek', '8-707-524-74-32', 'Tele2', 'meirambek@gmail.com', 'friend'],
]

with open('Phonebook.csv','w',newline='') as f:
   writer = csv.writer(f)
   writer.writerows(contact_list)



def from_csv_to_table():
   sql = """
      COPY phonebook(contact, tel_number, tel_connection, email, relationship)
      FROM \'C:\study\pp2\week10\phonebook'
      DELIMITER \',\'
      CSV HEADER;
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
   from_csv_to_table()
