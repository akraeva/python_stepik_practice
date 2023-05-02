# 5.15 Simple continued fraction

a, b = [int(i) for i in input().split('/')]
res = []
while b != 0:
    res.append(str(a//b))
    a, b = [b, a % b]
print(' '.join(res))
