import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
ch='y'
while ch=='y':
    pid=int(input("Enter parking ID = "))
    vehiclename=input("Enter Vehicle name  = ")
    vehicleno=input("Enter Vehicle no = ")
    vehicletype=input("Enter Vehicle type = ")
    cid = int(input("Enter cid ="))
    cur.execute("insert  into Parking values(%s,%s,%s,%s,%s) ",(pid,vehiclename,vehicleno,vehicletype,cid))
    con.commit()
    print("Your Record is inserted")
    ch = input("Do u want to continue(Y/N) = ")

con.close()
print("THANK YOU")