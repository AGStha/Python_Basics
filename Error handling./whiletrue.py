def ask_number():
    while True:
        try:
            a=int(input("enter number\n"))
        except:
            print("This is not number.")
            continue
        else:
            print("This is the number")
            break
        finally:
            print("Thanks")

ask_number()
