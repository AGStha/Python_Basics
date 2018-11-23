import sqlite3


con = sqlite3.connect("contacts.sqlite")
#We can check the schema. and attack by followin

#for row in con.execute("select *from sqlite_master"):
for row in con.execute("select * from contacts"):
    print(row)

con.close()
