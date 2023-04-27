# 3.6 Number sequence

length = int(input())
n = round((0.25 + 2 * length) ** 0.5)  # максимальное число
res = []
for i in range(n):
    res.extend([str(i+1) for j in range(i + 1)])
print(' '.join(res[0:length]))
