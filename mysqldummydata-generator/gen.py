import mysql.connector

host = input("Masukan host : ")
userdb = input("Masukan db user : ")
dbname = input("Masukan nama database : ")
dbpassword = input("Masukan password database : ")

mysqlconn = mysql.connector.connect(
host = host,
user = userdb,
database = dbname,
password = dbpassword
)

mycursor = mysqlconn.cursor()



query_fields = input("Masukan nama table yang ingin diisi : ")

# insert_query =





