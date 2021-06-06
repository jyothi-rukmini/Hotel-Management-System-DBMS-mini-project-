import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
ch='y'
while ch=='y':
    cid=int(input("Enter Customer ID = "))
    cname=input("Enter Customer Name = ")
    caddress=input("Enter Customer Address = ")
    cphno=int(input("Enter Customer Phno = "))
    cur.execute("insert  into Customers values(%s,%s,%s,%s) ",(cid,cname,caddress,cphno))
    con.commit()
    print("Your Record is inserted")
    ch = input("Do u want to continue(Y/N) = ")

con.close()
print("THANK YOU")