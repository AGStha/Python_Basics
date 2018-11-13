def add(a,b):
    return a+b

try:
    a=10
    b='a'
    c=add(a,b)
    print(c)
except:
    print("error")
finally:
    print("Thanks ")