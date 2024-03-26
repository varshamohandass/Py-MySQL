import mysql.connector

conn=mysql.connector.connect(host="localhost", user="root", password="admin", database = "softmania")
print(conn)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS softmania")
cursor.execute("CREATE TABLE IF NOT EXISTS person(id INT PRIMARY KEY, name VARCHAR(64))")
cursor.execute("CREATE TABLE IF NOT EXISTS THING(id INT PRIMARY KEY, name VARCHAR(64))")
cursor.execute(""" CREATE TABLE IF NOT EXISTS owns(
       person INT,
       thing INT,
       FOREIGN KEY (person) REFERENCES person(id),
       FOREIGN KEY (thing) REFERENCES thing(id)
       );""")

cursor.execute("SHOW TABLES")

for table in cursor:
    print(table)

# cursor.execute("""
#                INSERT INTO person (id,name) VALUES
#                (1,'Alice'),
#                (2,'Bob'),
#                (3,'Charlie')
#                """)
# cursor.execute("""
#                INSERT INTO thing (id,name) VALUES
#                (1,'Apple'),
#                (2,'Box'),
#                (3,'Computer')
#                """)
# cursor.execute("""
#                INSERT INTO owns (person,thing) VALUES
#                (1,2),
#                (2,3),
#                (3,1)
#                """)
with open("sqlcommands.txt","r") as file:
    lines=file.readlines()
for line in lines:
    cursor.execute(line)
conn.commit()
cursor.execute("SELECT * FROM softmania.thing")
for row in cursor:
    print(row)