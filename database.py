#import database libraty
import sqlite3
# define database connection
def db_connect():
 conn =sqlite3.connect('contact.db')
 return conn
#define database table
def create_db():
 conn = db_connect()
 with conn:
    cur = conn.cursor()
 query = "CREATE TABLE IF NOT EXISTS tbl_contactlist ("\
 "ID INTEGER PRIMARY KEY AUTOINCREMENT,"\
 "name TEXT,"\
 "email TEXT,"\
 "phone TEXT,"\
 "address TEXT)"
 cur.execute(query)
 conn.commit()
 conn.close()