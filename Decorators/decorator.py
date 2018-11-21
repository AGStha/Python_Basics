def func():
    print("hello")
func()
a=func
print(a())

#del func()
print(a())

def new_decorator(original_func):
    def wrap_func():
        print("code before original func")
        original_func()
        print("code after original func")
    return wrap_func
'''
def func_needs_decorator():
    print("I want to be decorated")



func_needs_decorator()

#we can pass
decorated_func=new_decorator(func_needs_decorator())

decorated_func()

'''


@new_decorator
def func_needs_decorator():
    print("I want to be decorated")
func_needs_decorator()