def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator 

@repeat(7)
def say_hello(a):
    print(f"Hello! {a}")
'''
it replaces the function say_hello with this:
def decorator(fun):
    def wrapper(a):
        for i in range(7)
            say_hello(simran)
    return wrapper        
'''
say_hello("simran")    

