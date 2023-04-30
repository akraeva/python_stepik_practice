# 3.2 Math function

def f(x):
    if x > 2:
        return (x - 2)**2 + 1
    elif x <= -2:
        return 1 - (x + 2)**2
    else:
        return (-1) * x / 2
