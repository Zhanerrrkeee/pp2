import psycopg2
from config import config

def get_telephone_numbers():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT contact, tel_number FROM phonebook ORDER BY contact")

        rows = cur.fetchall()

        print('Total number of contacts',cur.rowcount)
        for row in rows:
           print(row)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
   get_telephone_numbers()

# fetchall
