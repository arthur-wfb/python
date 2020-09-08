import math

def linear(a, b):
    return -b/a if a != 0 else None

def quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant >= 0:
        x_1=(-b+math.sqrt(discriminant))/2*a
        x_2=(-b-math.sqrt(discriminant))/2*a
    else:
        x_1= complex((-b/(2*a)),math.sqrt(-discriminant)/(2*a))
        x_2= complex((-b/(2*a)),-math.sqrt(-discriminant)/(2*a))

    if discriminant > 0:
        print(x_1, x_2)
    elif discriminant == 0:
        print(x_1)
    else:
        print(x_1, x_2)

def cubic(a, b, c, d):
