import sqlite3


db = sqlite3.connect("contacts.sqlite")

db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INT, email TEXT)")
db.execute("INSERT INTO contacts (name,phone,email) VALUES ('Anuj',22,'anuj@gmail.com')")
db.execute("Insert into contacts values ('Andrew', 2, 'juk@gmail.com')")


#We can display through cursor function.
cursor = db.cursor()
cursor.execute("select *from contacts")
"""for row in cursor:
    print(row)
"""
#cursor is the generator type of function.
"""
#fetchall method in cursor function which adds into the list so the generator doesnt work

#print(cursor.fetchall())

#Fetch One is used to pull single row.
print(cursor.fetchone())
print(cursor.fetchone())
print(cursor.fetchone())
"""
for name,phone,email in cursor:
    print(name)
    print(phone)
    print(email)
    print('-'*10)
cursor.close()
db.close()