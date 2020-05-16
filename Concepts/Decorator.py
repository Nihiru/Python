'''
:Decorators adds functionality to an existing code
:This is called as metaprogramming as a part of the program tries to modify anther part of the program at compile time.
:
'''
# basic functionality
def make_pretty(func):
    def inner():
        print("Decorator called")
        func()
    return inner

def ordinary():
    print("Ordinary called")

pretty = make_pretty(ordinary) # decorator 
# pretty()

# python implementation
@make_pretty
def ordinary2():
    print("I am ordinary 2")
ordinary2()

# parameterized decorators
def smart_divide(func):
    def inner(a, b):
        print(" I am going to divide", a, "and", b)
        if b == 0:
            print("whoops ! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(m,n):
    return m,n
divide(2, 5)

# chaining decorators in python
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)
printer("Hello")