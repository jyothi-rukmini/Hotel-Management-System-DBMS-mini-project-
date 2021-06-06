import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
cur.execute("select * from customers ")
res=cur.fetchall()
print("cno\t\tcname\tcaddress\t\tcphno")
print("---\t\t----\t-------\t\t\t-----")
for x in res:
    for y in x:
        print(y,end="\t")
    print()
con.close()