import sqlite3


db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INT, email TEXT)")
db.execute("INSERT INTO contacts (name,phone,email) VALUES ('Anuj',22,'anuj@gmail.com')")
db.execute("Insert into contacts values ('Andrew', 2, 'juk@gmail.com')")


#We can display through cursor function.
cursor = db.cursor()
cursor.execute("select *from contacts")
for row in cursor:
    print(row)

cursor.close()
db.close()