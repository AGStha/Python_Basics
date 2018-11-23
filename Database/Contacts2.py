import sqlite3


db = sqlite3.connect("contacts.sqlite")
#this is alt method to call the python sql without cursor function.

#Update using cursor
update_sql = "update contacts set email='changed@gmail.com' where contacts.name='Anuja'"

update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))
update_cursor.close()
for name, phone, email in db.execute("select *from contacts"):
    print(name)
    print(phone)
    print(email)
    print("_"*12)


db.close()