# '''
# LEGB
# Local, Enclosing, Global, Built-in
# '''

import builtins

x = 'global_x'
# print(dir(builtins))

# def min():
#     pass

# m = min([5,1,4,2,3])
# print(m)

# def test(z):
#     y = 'local_y'
#     x= "local x"
#     print(y)
#     print(z)
    
# test("local z")
# print(x)

def outer():
    x = 'outer x'
    
    def inner():
        x = 'inner x'
        print(x)
        
    inner()
    print(x)
    
outer()
print(x)