'''
:Nested functions can access variables of the enclosing scope
:The technique by which some data gets attached to the code is called closure
:When there are few methods to be implemented in a class, closures can provide an alternate and more elegant solutions
:Closure function can access values that are enclosed
'''

def printer_msg(msg):
    def inner_printer():
        print(msg) # accessing nonlocal variables
    inner_printer() # function call

    def closure_func():
        print(msg)
    return closure_func # returns an function object 

closure = printer_msg("hello")
closure() # call is made to inner function

# beauty
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))