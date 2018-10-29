List_of_users=['Anuj','Hari','Shyam','Bibika']

while True:
    print("hello my name is travis shrestha")
    name=input("What's your good name?").strip().capitalize()
    if name in List_of_users:
        print('Great!!{}'.format(name))
        remove=input("Your name is recognised \n would you like to remove(y/n)").strip().lower()
        if remove=='y':
            List_of_users.remove(name)
            print("Sorry {}".format(name),"See you Again")
        elif remove=='n':
            print("I did not want you to leave anyway")

    else:
        add=input("I couldn't find your name in the list.\n Would you like to add?(y/n)").strip().lower()
        if add=='y':
            List_of_users.append(name)
            print('your name is added',name)
        elif add=='n':
            print("thanks for connecting anyway")



