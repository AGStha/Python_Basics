try:
    f=open("test.txt",'w')

    f.write('hello')
    f.close()

    f=open("test.txt",'r')
    f.close()

    a=10+'10'
except TypeError:
    print("YOu have type error")
except OSError:
    print("YOu have os errror")
finally:
    print("thanks")