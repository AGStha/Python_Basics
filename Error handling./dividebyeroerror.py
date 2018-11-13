def divide(a,b):
    return a/b

try:
    a=int(input("First no."))
    b=int(input("Second no."))
    print(divide(a,b))
except:
    print("Divide by jero error.")
finally:
    print("Thanks")
