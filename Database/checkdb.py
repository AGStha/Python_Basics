import sqlite3


con = sqlite3.connect("contacts.sqlite")
for row in con.execute("select * from contacts"):
    print(row)

con.close()
