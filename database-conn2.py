from __future__ import print_function

import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='toor', db='mysql')

cur = conn.cursor()

cur.execute("show databases")
cur.execute("use final_store")
cur.execute("Insert into records(name, description) values(%s, %s)", ("Kaag", "Udyo"));

for row in cur:
        print(row)

conn.commit()
cur.close()
conn.close()
