# 1.10 Chained comparisons

def t():
    print('t')
    return True


def f():
    print('f')
    return False


x = 0
if f() < t() < f():
    x += 1

if f() < t() and t() < f():
    x += 1
