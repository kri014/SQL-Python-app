import mysql.connector

# connect to the database server
try:
    conn= mysql.connector.connect(
        host = "127.0.0.1",
        user = "root",
        password = "",
        database = "indigo"
     )
    mycursor = conn.cursor()
    print("Connection Establish")
except:
    print("Connection Error ")

# create dabase in db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table
# Airport -> airport_id, code, name, city
#mycursor.execute ("""
#        CREATE TABLE airport(
#        airport_id INTEGER PRIMARY KEY,
#        code VARCHAR(10) NOT NULL,
#       name VARCHAR(50) NOT NULL,
#       city VARCHAR(255) NOT NULL
#       )
#       """
#      )
#  conn.commit()

# ADD some data in table
#mycursor.execute("""
        #INSERT INTO airport VALUES
        #(1,"DEL","New Delhi","IGIA"),
        #(2,"CCU","kolkata","NSA"),
        #(3,"BOM","mumbai","CSAT")
        #""")
#conn.commit()

# search /retrive the data
mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data=mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# update
mycursor.execute("""
            UPDATE airport 
            SET name= "Bombay"
            WHERE airport_id =3
            """)
conn.commit()

mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data=mycursor.fetchall()
print(data)

for i in data:
    print(i[3])

# Delete
mycursor.execute(" DELETE FROM airport WHERE airport_id =3")
conn.commit()

mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data=mycursor.fetchall()
print(data)
