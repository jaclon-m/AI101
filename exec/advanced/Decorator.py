from math import sqrt

def get_int(f):
    def inner(x):
        x = int(x)
        return f(x)
    return inner

def get_abs(f):
    def inner(x):
        x = abs(x)
        return f(x)
    return inner

@get_int
@get_abs
def func(x):
    return sqrt(x)

print(func(-4))