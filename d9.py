import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
ch='y'
while ch=='y':
    rno=int(input("Enter room no = "))
    rtype=input("Enter room type(single/double)  = ")
    noofbeds=int(input("Enter noofbeds = "))
    floorno=int(input("Enter floor no = "))
    cid=int(input("Enter cid ="))
    cur.execute("insert  into rooms values(%s,%s,%s,%s,%s) ",(rno,rtype,noofbeds,floorno,cid))
    con.commit()
    print("Your Record is inserted")
    ch = input("Do u want to continue(Y/N) = ")

con.close()
print("THANK YOU")