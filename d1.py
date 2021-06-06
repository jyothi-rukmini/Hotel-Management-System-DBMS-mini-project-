import  mysql.connector  as mysql
con = mysql.connect(user="root",password="JyoRuk@36029",host="localhost",port="3306",database="jyothi_dbms")
print(" Connection is Established ")
cur = con.cursor()
print(con)
