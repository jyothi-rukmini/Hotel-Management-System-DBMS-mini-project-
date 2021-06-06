import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
ch='y'
while ch=='y':
    ftype=input("Enter food type = ")
    fname=input("Enter food name  = ")
    fcost=float(input("Enter food cost = "))
    cid = int(input("Enter cid ="))
    cur.execute("insert  into Foods values(%s,%s,%s,%s) ",(ftype,fname,fcost,cid))
    con.commit()
    print("Your Record is inserted")
    ch = input("Do u want to continue(Y/N) = ")

con.close()
print("THANK YOU")