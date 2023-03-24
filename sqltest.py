import mysql.connector

conn=mysql.connector.connect(host="localhost",username="root",password="THEVIRTUALEYE",port="3306",database="ayush")

my_cursor=conn.cursor()
my_cursor.execute('insert into users values(%s,%s,%s)',('ayush','sharma','123'))
conn.commit()
conn.close()