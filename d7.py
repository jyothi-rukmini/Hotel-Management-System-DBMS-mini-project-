import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
ch='y'
while ch=='y':
    wid=int(input("Enter Worker ID = "))
    wname=input("Enter Worker Name = ")
    wsalary=float(input("Enter Worker Salary = "))
    wphno=int(input("Enter Worker Phno = "))
    cur.execute("insert  into Workers values(%s,%s,%s,%s) ",(wid,wname,wsalary,wphno))
    con.commit()
    print("Your Record is inserted")
    ch = input("Do u want to continue(Y/N) = ")

con.close()
print("THANK YOU")
