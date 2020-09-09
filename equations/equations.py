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

def cube(a=0, b=0, c=0, d=0):
    if a == 0:
        return square(b, c, d)
    if a == 0 and b == 0:
        return line(c, d)
    if not (a == 0) and (d == 0):
        dis = -4 * b ** 3 * d + b ** 2 * c ** 2 - 4 * a * c ** 3 + 18 * a * b * c * d - 27 * a ** 2 * d ** 2
        if dis > 0:
            x1 = 0
            x2 = (-b + d ** 0.5) / (2 * a)
            x3 = (-b - d ** 0.5) / (2 * a)
            return [x1, x2, x3]
        if dis == 0:
            x2 = -b / (2 * a)
            return [x2]
    p = (3 * a * c - b ** 2) / (3 * a ** 2)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3)
    S = (4 * (3 * a * c - b ** 2) ** 3 + (2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) * (
            2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d)) / (2916 * a ** 6)
    y1 = 0
    y2 = 0
    if S < 0:
        if q < 0:
            t = m.atan(-2 * (-S ** 0.5) / q)
            if q > 0:
                t = m.atan(-2 * (-S ** 0.5) / q) + m.pi
            if q == 0:
                t = m.pi / 2
            x1 = 2 * (-p / 3) ** 0.5 * m.cos(t / 3) - b / (3 * a)
            x2 = 2 * (-p / 3) ** 0.5 * m.cos((t + 2 * m.pi) / 3) - b / (3 * a)
            x3 = 2 * (-p / 3) ** 0.5 * m.cos((t + 4 * m.pi) / 3) - b / (3 * a)
            if q == 0:
                x3 = -b / (3 * a)
            return [x1, x2, x3]
    elif S > 0:
        if (-q / 2 + S ** 0.5) > 0:
            y1 = m.exp(m.log(m.fabs(-q / 2 + S ** 0.5)) / 3)
        if (-q / 2 + S ** 0.5) < 0:
            y1 = -m.exp(m.log(m.fabs(-q / 2 + S ** 0.5)) / 3)
        if (-q / 2 + S ** 0.5) == 0:
            y1 = 0
        if (-q / 2 - S ** 0.5) > 0:
            y2 = m.exp(m.log(m.fabs(-q / 2 - S ** 0.5)) / 3)
        if (-q / 2 - S ** 0.5) < 0:
            y2 = -m.exp(m.log(m.fabs(-q / 2 - S ** 0.5)) / 3)
        if (-q / 2 - S ** 0.5) == 0:
            y2 = 0
        Re1 = -(y1 + y2) / 2 - b / a / 3
        Im1 = (y1 - y2) * 3 ** 0.5 / 2
        x1 = y1 + y2 - b / a / 3
        x2 = complex(Re1, Im1)
        x3 = complex(Re1, -Im1)
        return [x1, x2, x3]
    elif S == 0:
        if q < 0:
            y1 = m.exp(m.log(m.fabs(-q / 2)) / 3)
        if q > 0:
            y1 = -m.exp(m.log(m.fabs(-q / 2)) / 3)
        if q == 0:
            y1 = 0
        x1 = 2 * y1 - b / a / 3
        x2 = -y1 - b / a / 3
        x3 = -y1 - b / a / 3
        return [x1, x2, x3]
    return []
