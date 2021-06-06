import mysql.connector as mysql
con = mysql.connect(user='root', password='JyoRuk@36029', host='localhost', port='3306', database='jyothi_dbms')
cur=con.cursor()
cur.execute("select * from workers ")
res=cur.fetchall()
print("wid\t\twname\twsalary\t\twphno")
print("---\t\t------\t-------\t\t-----")
for x in res:
    for y in x:
        print(y,end="\t\t")
    print()
con.close()