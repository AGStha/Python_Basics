import sqlite3


db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE contacts (name text, phone int, email text)")
db.execute("INSERT INTO contacts (name,phone,email) VALUES ('Anuj',22,'anuj@gmail.com')")
db.execute("Insert into contacts values ('Andrew', 2, 'juk@gmail.com')")

db.close()