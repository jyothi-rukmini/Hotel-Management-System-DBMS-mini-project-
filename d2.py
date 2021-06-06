import mysql.connector as mysql
print("~~~~~HOTEL MANAGEMENT SYSTEM~~~~~")
try:
    con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
    cur=con.cursor()  #cursor gives connection between mysql and python
    cur.execute("create table Workers(wid integer,wname text,wsalary real,wphno real)")
    print("table is created")
    con.commit()
except:
    print("Unable to create connection")
else:
    con.close()
