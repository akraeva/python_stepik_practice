# 3.5 Cache function

# lib functools : @cache или @lru_cache(maxsize=None)
def f(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return (f(x - 1) + f(x - 2)) * 13 % 107


n = int(input())
cch = {}
for i in range(n):
    num = int(input())
    if num not in cch:
        cch[num] = f(num)
    print(cch[num])
