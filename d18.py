cid=int(input("Enter Customer ID = "))
import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
cur.execute("delete from customers where cid = %s ",(cid,))
con.commit()
print("Record is deleted")
con.close()
