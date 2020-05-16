'''
:Nested functions can access variables of the enclosing scope
:The technique by which some data gets attached to the code is called closure
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