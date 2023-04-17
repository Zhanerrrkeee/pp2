import psycopg2
from config import config

def get_telephone_numbers():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT contact, tel_number FROM phonebook ORDER BY contact")

        row = cur.fetchone()

        print('Total count of contacts:',cur.rowcount)
        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    get_telephone_numbers()
