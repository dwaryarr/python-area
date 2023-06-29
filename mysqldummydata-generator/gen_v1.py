import mysql.connector
import random
import string

# Membaca input dari pengguna
host = input("Masukkan host: ")
userdb = input("Masukkan db user: ")
dbname = input("Masukkan nama database: ")
dbpassword = input("Masukkan password database: ")
table_name = input("Masukkan nama tabel yang ingin diisi: ")
num_records = int(input("Masukkan jumlah record yang ingin digenerate: "))

# Membuat koneksi ke database
mysqlconn = mysql.connector.connect(
    host=host,
    user=userdb,
    database=dbname,
    password=dbpassword
)

mycursor = mysqlconn.cursor()

# Mengambil informasi kolom dari tabel
mycursor.execute("DESCRIBE {}".format(table_name))
columns = mycursor.fetchall()
column_names = [column[0] for column in columns]

# Generate dan masukkan data dummy ke tabel
for _ in range(num_records):
    record_values = []
    for column_name in column_names:
        if column_name == 'id':
            # Jika kolom adalah 'id', berikan nilai NULL agar nilai otomatis digenerate
            record_values.append("NULL")
        else:
            # Jika kolom bukan 'id', buat data dummy acak
            if 'varchar' in column_name.lower():
                # Jika kolom adalah varchar, buat string acak
                random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
                record_values.append("'{}'".format(random_string))
            elif 'int' in column_name.lower():
                # Jika kolom adalah integer, buat nilai acak antara 1 dan 100
                random_int = random.randint(1, 100)
                record_values.append(str(random_int))
            elif 'float' in column_name.lower():
                # Jika kolom adalah float, buat nilai acak antara 0.0 dan 1.0
                random_float = random.uniform(0.0, 1.0)
                record_values.append(str(random_float))

    # Masukkan record ke dalam tabel
    insert_query = "INSERT INTO {} ({}) VALUES ({});".format(table_name, ", ".join(column_names), ", ".join(record_values))
    mycursor.execute(insert_query)
    mysqlconn.commit()

# Menutup koneksi ke database
mysqlconn.close()
