cid=int(input("Enter Customer ID = "))
cname=input("Enter Customer Name = ")
import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
cur.execute("update customers set cname = %s where cid=%s",(cname,cid))
con.commit()
print("Record is updated")
con.close()
