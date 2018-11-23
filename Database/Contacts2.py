import sqlite3


db = sqlite3.connect("contacts.sqlite")
#this is alt method to call the python sql without cursor function.

#Update using cursor

#update_sql = "update contacts set email='changed@gmail.com' where contacts.name='Anuj'"

#Using placeholder method/ pass through user input.
email='sqlinject@gmail.com'
phone=input("enter the phone")
update_sql = "update contacts set email='{}' where phone={}".format(email,phone)


update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount))

print()
print("Are the connection same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()
for name, phone, email in db.execute("select *from contacts"):
    print(name)
    print(phone)
    print(email)
    print("_"*12)


db.close()