import psycopg2 as pg2

conn=pg2.connect(database='sql_intro',user='postgres',password='sudarshan09',port=5432)

cur=conn.cursor()

a=cur.execute('select * from tata_emp')

cur.fetchmany(4)