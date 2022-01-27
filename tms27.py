import mysql.connector as mysql

db = mysql.connect(host="localhost",
                    user="root",
                    passwd="deadbyarms187",
                    database="test_db")

cursor = db.cursor()
# cursor.execute("CREATE DATABASE test_db")

cursor.execute("SHOW DATABASES")
print(cursor.fetchall())


# cursor.execute("CREATE TABLE users (name VARCHAR(255), user_name VARCHAR(255))")
# cursor.execute("SHOW TABLES")
# cursor.execute("ALTER TABLE users ADD COLUMN id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY FIRST")
# cursor.execute("DESC users")

# query = "INSERT INTO users (name, user_name) VALUES (%s, %s)"
# values = ("hello", "hello1")
# cursor.execute(query, values)
# db.commit()

# print(cursor.rowcount, "record inserted")
# print(cursor.fetchall())

query = 'select * from users'
cursor.execute(query)
print(cursor.fetchall())