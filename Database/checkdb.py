import sqlite3


con = sqlite3.connect("contacts.sqlite")
#We can check the schema. and attack by followin
name=input("Enter the name")
#con=sqlite3.connect("contacts.sqlite3")
#for row in con.execute("select * from contacts where name=?",(name,)):
for row in con.execute("select * from contacts where name like ?", (name,)):  #(name,) Parameter sustitution.and ? is place holder
    print(row)

#for  row in con.execute("select *from sqlite_master"):
"""for row in con.execute("select * from contacts"):
    print(row)
"""
con.close()
