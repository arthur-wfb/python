def find(x1, x2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            delata = 0.0001
            maxValue = 999
            nonlocal x1
            nonlocal x2
            x = x1 + abs((x2-x1)/2)
            while abs(func(x) - func(x + delata)) < maxValue:
                if abs(func(x) - func(x1)) < abs((func(x) - func(x2))):
                    x1 = x
                else:
                    x2 =x
                x = x1 + abs((x2-x1)/2)
            return x
        return wrapper
    return decorator

@find(x1=-3, x2=6)
def f(x):
    return 1/x

print(f())