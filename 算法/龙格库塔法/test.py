def func1(*x):
    return x[0]**2

def func2(func, *x):
    return func(*x)

print(func2(func1, 5., 6.))